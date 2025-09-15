import sys
from typing import List, Optional
from .models import MenuCategory
from .recommender import MenuRecommender


def print_menu_list(menus: List, title: str = "추천 메뉴"):
    """메뉴 리스트를 예쁘게 출력합니다."""
    print(f"\n🍽️ {title}")
    print("=" * 40)
    for i, menu in enumerate(menus, 1):
        tags_str = ", ".join(menu.tags)
        spice_emoji = "🌶️" * menu.spicy_level if menu.spicy_level > 0 else ""
        print(f"{i}. {menu.name}")
        print(f"   카테고리: {menu.category.value}")
        print(f"   가격대: {menu.price_range} | 조리시간: {menu.prep_time}분 {spice_emoji}")
        print(f"   특징: {tags_str}")
        print()


def get_user_input(prompt: str) -> str:
    """사용자 입력을 받습니다."""
    try:
        return input(prompt).strip()
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
        sys.exit(0)


def get_category_choice() -> Optional[MenuCategory]:
    """카테고리 선택을 받습니다."""
    categories = list(MenuCategory)
    print("\n📝 원하는 음식 카테고리를 선택하세요:")
    print("0. 상관없음")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.value}")

    choice = get_user_input("선택 (숫자): ")
    if choice == "0" or not choice:
        return None
    try:
        return categories[int(choice) - 1]
    except (ValueError, IndexError):
        print("잘못된 선택입니다.")
        return None


def get_price_choice() -> Optional[str]:
    """가격대 선택을 받습니다."""
    prices = ["저렴", "보통", "비싸"]
    print("\n💰 원하는 가격대를 선택하세요:")
    print("0. 상관없음")
    for i, price in enumerate(prices, 1):
        print(f"{i}. {price}")

    choice = get_user_input("선택 (숫자): ")
    if choice == "0" or not choice:
        return None
    try:
        return prices[int(choice) - 1]
    except (ValueError, IndexError):
        print("잘못된 선택입니다.")
        return None


def get_spice_level() -> Optional[int]:
    """매운 정도 선택을 받습니다."""
    print("\n🌶️ 매운 정도를 선택하세요 (0-5):")
    print("0. 안매움  1. 약간매움  2. 보통매움  3. 매움  4. 많이매움  5. 매우매움")
    print("선택하지 않으려면 엔터를 누르세요")

    choice = get_user_input("선택 (숫자): ")
    if not choice:
        return None
    try:
        level = int(choice)
        return level if 0 <= level <= 5 else None
    except ValueError:
        print("잘못된 입력입니다.")
        return None


def get_tags() -> List[str]:
    """선호 태그를 받습니다."""
    available_tags = ["건강한", "든든한", "가벼운", "따뜻한", "시원한", "매운", "달콤한",
                     "바삭한", "부드러운", "간단한", "빠른", "고급스러운"]

    print("\n🏷️ 원하는 음식 특징을 선택하세요 (여러 개 선택 가능):")
    print("0. 상관없음")
    for i, tag in enumerate(available_tags, 1):
        print(f"{i}. {tag}")

    print("예: 1,3,5 (쉼표로 구분)")
    choice = get_user_input("선택: ")

    if choice == "0" or not choice:
        return []

    try:
        indices = [int(x.strip()) - 1 for x in choice.split(",")]
        return [available_tags[i] for i in indices if 0 <= i < len(available_tags)]
    except (ValueError, IndexError):
        print("잘못된 선택입니다.")
        return []


def get_prep_time() -> Optional[int]:
    """조리시간 제한을 받습니다."""
    print("\n⏰ 최대 조리시간을 입력하세요 (분):")
    print("예: 15 (15분 이내), 상관없으면 엔터")

    choice = get_user_input("시간 (분): ")
    if not choice:
        return None
    try:
        return int(choice)
    except ValueError:
        print("잘못된 입력입니다.")
        return None


def main_menu():
    """메인 메뉴를 표시합니다."""
    print("\n🍽️ 점심메뉴 추천 서비스")
    print("=" * 30)
    print("1. 랜덤 추천")
    print("2. 조건별 추천")
    print("3. 빠른 식사 추천")
    print("4. 종료")

    return get_user_input("선택: ")


def main():
    """메인 함수"""
    recommender = MenuRecommender()

    print("🎉 점심메뉴 추천 서비스에 오신 것을 환영합니다!")

    while True:
        choice = main_menu()

        if choice == "1":
            # 랜덤 추천
            count = 3
            try:
                count_input = get_user_input("추천받을 메뉴 개수 (기본 3개): ")
                if count_input:
                    count = int(count_input)
            except ValueError:
                pass

            menus = recommender.recommend_random(count)
            print_menu_list(menus, "랜덤 추천 메뉴")

        elif choice == "2":
            # 조건별 추천
            print("\n🔍 조건을 선택해주세요:")

            category = get_category_choice()
            price_range = get_price_choice()
            max_spice = get_spice_level()
            preferred_tags = get_tags()
            max_prep_time = get_prep_time()

            try:
                count_input = get_user_input("\n추천받을 메뉴 개수 (기본 3개): ")
                count = int(count_input) if count_input else 3
            except ValueError:
                count = 3

            menus = recommender.recommend_comprehensive(
                category=category,
                price_range=price_range,
                max_spice=max_spice,
                preferred_tags=preferred_tags,
                max_prep_time=max_prep_time,
                count=count
            )
            print_menu_list(menus, "조건별 추천 메뉴")

        elif choice == "3":
            # 빠른 식사 추천
            max_time = 15
            try:
                time_input = get_user_input("최대 조리시간 (기본 15분): ")
                if time_input:
                    max_time = int(time_input)
            except ValueError:
                pass

            menus = recommender.recommend_quick_meal(max_time)
            print_menu_list(menus, f"{max_time}분 이내 빠른 식사")

        elif choice == "4":
            print("\n👋 맛있는 식사 되세요!")
            break

        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

        input("\n계속하려면 엔터를 누르세요...")


if __name__ == "__main__":
    main()