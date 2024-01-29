from dateparser import parse
from ru_word2number.w2n import word_to_num

from src.abstracts.date_normalizer import AbstractDateNormalizer
from src.common.exceptions import InvalidDateException


class DateNormalizer(AbstractDateNormalizer):
    @classmethod
    async def normalize(cls, tree: dict) -> None:
        for key, value in tree.items():
            if isinstance(value, dict):
                await cls.normalize(value)
            if "дата" in key.lower():
                tree[key] = await cls.__convert_string_to_date(date_string=value)
            if "срок" in key.lower():
                tree[key] = await cls.__calculate_remained_term(deadline=value)

    @classmethod
    async def __convert_string_to_date(cls, date_string: str) -> str:
        date = parse(date_string, languages=["ru"])
        if date is None:
            raise InvalidDateException("Invalid Date Format")
        formatted_date = date.strftime("%d.%m.%Y")
        return formatted_date

    @classmethod
    async def __calculate_remained_term(cls, deadline: str) -> str:
        left = 0
        term_dict = {
            "years": 0,
            "months": 0,
            "weeks": 0,
            "days": 0
        }
        split_deadline = deadline.split()
        if "полгода" in split_deadline:
            term_dict["months"] += 6
        if "полтора года" in deadline:
            term_dict["years"] += 1
            term_dict["months"] += 6
        if "полтора месяца" in deadline:
            term_dict["months"] += 1
            term_dict["weeks"] += 2

        for index, word in enumerate(split_deadline):
            possible_number = split_deadline[index - 1]
            if ("лет" in word.lower() or "год" in word.lower()) and "полгода" not in word.lower():
                if possible_number == "полтора":
                    continue
                number = await cls.__get_number(possible_number=possible_number,
                                                word_range=split_deadline[left:index + 1])
                term_dict["years"] += number
                left = index
            elif "месяц" in word.lower():
                if possible_number == "полтора":
                    continue
                number = await cls.__get_number(possible_number=possible_number,
                                                word_range=split_deadline[left:index + 1])
                term_dict["months"] += number
                left = index
            elif (
                    "недели" in word.lower() or
                    "недель" in word.lower() or
                    "неделя" in word.lower()
            ):
                number = await cls.__get_number(possible_number=possible_number,
                                                word_range=split_deadline[left:index + 1])
                term_dict["weeks"] += number
                left = index
            elif (
                    "день" in word.lower() or
                    "дней" in word.lower() or
                    "дня" in word.lower()
            ):
                number = await cls.__get_number(possible_number=possible_number,
                                                word_range=split_deadline[left:index + 1])
                term_dict["days"] += number
                left = index
        return "_".join(map(str, term_dict.values()))

    @classmethod
    async def __convert_word_to_number(cls, split_deadline: list[str]) -> int | None:
        start = 0
        was_the_number = False
        for index, word in enumerate(split_deadline):
            try:
                word_to_num(word)
            except ValueError:
                if not was_the_number:
                    continue
                return word_to_num(" ".join(split_deadline[start:index + 1]))
            else:
                if not was_the_number:
                    start = index
                    was_the_number = True

    @classmethod
    async def __get_number(cls, possible_number: str, word_range: list[str]) -> int:
        try:
            number = int(possible_number)
        except ValueError:
            if possible_number == "одна":
                # Так как функция word_to_num() не конвертирует "одна" в 1
                return 1
            number = await cls.__convert_word_to_number(split_deadline=word_range)
        return number
