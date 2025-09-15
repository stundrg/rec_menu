import random
from typing import List, Optional
from .models import Menu, MenuCategory
from .menu_data import MENU_DATABASE


class MenuRecommender:
    def __init__(self):
        self.menus = MENU_DATABASE

    def recommend_random(self, count: int = 1) -> List[Menu]:
        """랜덤으로 메뉴를 추천합니다."""
        return random.sample(self.menus, min(count, len(self.menus)))

    def recommend_by_category(self, category: MenuCategory, count: int = 3) -> List[Menu]:
        """특정 카테고리의 메뉴를 추천합니다."""
        category_menus = [menu for menu in self.menus if menu.category == category]
        return random.sample(category_menus, min(count, len(category_menus)))

    def recommend_by_price(self, price_range: str, count: int = 3) -> List[Menu]:
        """가격대별로 메뉴를 추천합니다."""
        price_menus = [menu for menu in self.menus if menu.price_range == price_range]
        return random.sample(price_menus, min(count, len(price_menus)))

    def recommend_by_spice_level(self, max_spice: int, count: int = 3) -> List[Menu]:
        """매운 정도에 따라 메뉴를 추천합니다."""
        spice_menus = [menu for menu in self.menus if menu.spicy_level <= max_spice]
        return random.sample(spice_menus, min(count, len(spice_menus)))

    def recommend_by_tags(self, preferred_tags: List[str], count: int = 3) -> List[Menu]:
        """선호하는 태그에 따라 메뉴를 추천합니다."""
        scored_menus = []

        for menu in self.menus:
            score = sum(1 for tag in preferred_tags if tag in menu.tags)
            if score > 0:
                scored_menus.append((menu, score))

        # 점수순으로 정렬하고 상위 메뉴들을 반환
        scored_menus.sort(key=lambda x: x[1], reverse=True)
        top_menus = [menu for menu, score in scored_menus[:count*2]]

        # 같은 점수 내에서 랜덤 선택
        return random.sample(top_menus, min(count, len(top_menus)))

    def recommend_quick_meal(self, max_prep_time: int = 15, count: int = 3) -> List[Menu]:
        """빠른 식사를 원할 때 추천합니다."""
        quick_menus = [menu for menu in self.menus if menu.prep_time <= max_prep_time]
        return random.sample(quick_menus, min(count, len(quick_menus)))

    def recommend_comprehensive(self,
                              category: Optional[MenuCategory] = None,
                              price_range: Optional[str] = None,
                              max_spice: Optional[int] = None,
                              preferred_tags: Optional[List[str]] = None,
                              max_prep_time: Optional[int] = None,
                              count: int = 3) -> List[Menu]:
        """다양한 조건을 종합하여 메뉴를 추천합니다."""
        filtered_menus = self.menus.copy()

        # 카테고리 필터링
        if category:
            filtered_menus = [menu for menu in filtered_menus if menu.category == category]

        # 가격대 필터링
        if price_range:
            filtered_menus = [menu for menu in filtered_menus if menu.price_range == price_range]

        # 매운 정도 필터링
        if max_spice is not None:
            filtered_menus = [menu for menu in filtered_menus if menu.spicy_level <= max_spice]

        # 조리시간 필터링
        if max_prep_time:
            filtered_menus = [menu for menu in filtered_menus if menu.prep_time <= max_prep_time]

        # 태그 기반 점수 계산
        if preferred_tags:
            scored_menus = []
            for menu in filtered_menus:
                score = sum(1 for tag in preferred_tags if tag in menu.tags)
                scored_menus.append((menu, score))

            # 점수가 있는 메뉴들을 우선 선택
            scored_menus.sort(key=lambda x: x[1], reverse=True)
            if scored_menus and scored_menus[0][1] > 0:
                top_score = scored_menus[0][1]
                top_menus = [menu for menu, score in scored_menus if score == top_score]
                return random.sample(top_menus, min(count, len(top_menus)))

        # 조건에 맞는 메뉴가 있으면 랜덤 선택
        if filtered_menus:
            return random.sample(filtered_menus, min(count, len(filtered_menus)))

        # 조건에 맞는 메뉴가 없으면 전체에서 랜덤 선택
        return self.recommend_random(count)