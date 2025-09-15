from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class MenuCategory(Enum):
    KOREAN = "한식"
    CHINESE = "중식"
    JAPANESE = "일식"
    WESTERN = "양식"
    SNACK = "분식"
    FAST_FOOD = "패스트푸드"
    DESSERT = "디저트"


@dataclass
class Menu:
    name: str
    category: MenuCategory
    price_range: str  # "저렴", "보통", "비싸"
    spicy_level: int  # 0-5 (0: 안매움, 5: 매우매움)
    prep_time: int  # 조리시간 (분)
    tags: List[str]  # ["건강한", "든든한", "가벼운", "따뜻한", "시원한"]

    def __str__(self):
        return f"{self.name} ({self.category.value})"