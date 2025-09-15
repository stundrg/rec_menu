#!/usr/bin/env python3

from src.rec_menu import MenuRecommender, MenuCategory

def demo():
    print("🎉 점심메뉴 추천 서비스 데모")
    print("=" * 40)

    recommender = MenuRecommender()

    # 1. 랜덤 추천 데모
    print("\n🎲 랜덤 추천 3개:")
    random_menus = recommender.recommend_random(3)
    for i, menu in enumerate(random_menus, 1):
        print(f"{i}. {menu.name} ({menu.category.value}) - {menu.price_range}")

    # 2. 한식 추천 데모
    print("\n🍚 한식 추천 3개:")
    korean_menus = recommender.recommend_by_category(MenuCategory.KOREAN, 3)
    for i, menu in enumerate(korean_menus, 1):
        tags_str = ", ".join(menu.tags)
        print(f"{i}. {menu.name} - {tags_str}")

    # 3. 저렴한 메뉴 추천
    print("\n💰 저렴한 메뉴 3개:")
    cheap_menus = recommender.recommend_by_price("저렴", 3)
    for i, menu in enumerate(cheap_menus, 1):
        print(f"{i}. {menu.name} ({menu.category.value}) - {menu.prep_time}분")

    # 4. 빠른 식사 추천
    print("\n⚡ 10분 이내 빠른 식사:")
    quick_menus = recommender.recommend_quick_meal(10, 3)
    for i, menu in enumerate(quick_menus, 1):
        print(f"{i}. {menu.name} - {menu.prep_time}분")

    # 5. 조건별 추천 (건강한 + 가벼운)
    print("\n🥗 건강하고 가벼운 메뉴:")
    healthy_menus = recommender.recommend_by_tags(["건강한", "가벼운"], 3)
    for i, menu in enumerate(healthy_menus, 1):
        tags_str = ", ".join(menu.tags)
        print(f"{i}. {menu.name} ({menu.category.value}) - {tags_str}")

if __name__ == "__main__":
    demo()