# Plan — Bowling Game Kata

Game 클래스(`roll(pins)`, `score()`)를 Python + pytest로 TDD 구현한다. 각 항목은 RED(테스트 작성) → 리뷰 → GREEN(구현) → 리뷰 → REFACTOR 순으로 진행한다.

## 테스트 항목 순서 (계획)

| # | 테스트 이름 | 검증할 동작 |
|---|---|---|
| 1 | `test_gutter_game_scores_zero` | 20번 투구 모두 0핀 → 총점 0 |
| 2 | `test_all_ones_scores_twenty` | 20번 투구 모두 1핀 → 총점 20 (open frame 합산 확인) |
| 3 | `test_one_spare` | 한 프레임만 스페어(예: 5+5), 나머지는 0 → 스페어 보너스(다음 1투구) 확인 |
| 4 | `test_one_strike` | 한 프레임만 스트라이크, 나머지는 0 → 스트라이크 보너스(다음 2투구) 확인 |
| 5 | `test_all_spares_scores_150` | 모든 프레임 5+5 스페어, 10번 프레임 보너스 5 → 총점 150 |
| 6 | `test_perfect_game` | 12번 모두 스트라이크(퍼펙트 게임) → 총점 300 |
| 7 | `test_nine_and_spare` | 9,1 스페어 뒤 3 → 해당 프레임 13점 등 조합 확인 |
| 8 | `test_spare_in_tenth_frame_gets_one_bonus_roll` | 10번 프레임에서 스페어 → 보너스 투구 1회 허용 및 합산 확인 |
| 9 | `test_strike_in_tenth_frame_gets_two_bonus_rolls` | 10번 프레임에서 스트라이크 → 보너스 투구 2회 허용 및 합산 확인 |
| 10 | `test_strike_followed_by_spare` | 스트라이크 다음 프레임이 스페어인 경우 보너스 연쇄 계산 확인 |
| 11 | `test_two_consecutive_strikes` | 연속 스트라이크 2회 후 open frame → 보너스 중첩 계산 확인 |
| 12 | `test_strike_in_ninth_chains_into_tenth_frame_spare` | 9번 프레임 스트라이크가 10번 프레임(스페어) 투구까지 보너스로 참조하는 경계 케이스 |

## 구현 구조 (설계 방향)

- **자료구조**: 프레임/보너스를 별도 클래스로 모델링하지 않는다. `Game`은 `self._rolls: list[int]` 하나만 들고, `roll(pins)`는 단순히 `self._rolls.append(pins)` 한다.
  - Frame 객체, Roll 객체 등은 만들지 않는다 — 이 카타의 핵심은 "굴린 순서(투구 리스트)"만으로 점수를 계산하는 것이고, 프레임 경계는 `score()`가 계산 중에만 사용하는 인덱스일 뿐이다.
- **`score()` 알고리즘** (Uncle Bob의 고전적인 배열 기반 방식):
  - `self._rolls` 위를 인덱스 `i`로 훑으면서 10개 프레임을 순회한다.
  - 각 프레임에서:
    - 스트라이크(`rolls[i] == 10`): 프레임 점수 = `10 + rolls[i+1] + rolls[i+2]`, `i`는 1만 전진.
    - 스페어(`rolls[i] + rolls[i+1] == 10`): 프레임 점수 = `10 + rolls[i+2]`, `i`는 2 전진.
    - 오픈 프레임: 프레임 점수 = `rolls[i] + rolls[i+1]`, `i`는 2 전진.
  - 10번 프레임의 보너스 투구(있다면)는 `self._rolls`에 이미 이어서 들어 있으므로, 위 로직의 "다음 투구 조회(look-ahead)"가 인덱스 범위 안에서 자연스럽게 처리된다 — 10번째 프레임을 특별 케이스로 분기하지 않는다.
  - 즉 프레임 반복은 정확히 10번만 수행하고, 그 이후(보너스 투구)는 별도로 순회하지 않는다.
- **왜 이 구조인가**: 별도 `Frame` 클래스나 상태 머신 없이도 각 테스트 항목(스페어/스트라이크/10번 프레임 보너스)이 모두 "다음 1~2개 투구를 조회하는 오프셋 계산"으로 환원되기 때문에, 리스트 인덱싱만으로 충분하다. 필요 이상으로 추상화하지 않는다.
- 이 구조가 감당하기 어려워지는 시점(예: 프레임별 중간 점수를 노출해야 하는 요구가 생기는 경우)이 오면 그때 `Frame` 개념을 도입하는 것으로 미룬다.
