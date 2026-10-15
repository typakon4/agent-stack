# Проверка общих дизайн-targets — 2026-10-15

Текущая ревизия переносимости — 2. Предыдущий отчёт относится к коммиту 9c6c604 и сохранён в [initial-integration-verification.md](provenance/initial-integration-verification.md).

## Изменения

- Все 30 дизайн-навыков находятся в `shared/skills`; targets — Hermes / OMP / Codex, статус — optional.
- 29 ранее импортированных entrypoints получили границу возможностей host. Ресурсы, лицензии и три файла metadata сохранены без изменений. `source-lock.json` содержит исходные `reviewed_codex_files` и текущие `files` SHA-256.
- Общий `design-routing-fragment` перенесён в `shared/instructions/design-routing.md`; статус manual, без применения установщиком. Имя прежнего компонента `codex-design-routing-fragment` заменено этим общим именем; установленный ранее файл в профиле автоматически не удаляется и не заменяется.
- Основной README переведён на русский. Добавлена [инструкция Codex Cloud](../docs/codex-cloud.md) с текстом передачи контекста. Облачная среда не создавалась.
- Первые девять manifest-компонентов, Jev pin и код установщика не изменены.

## Наблюдённые проверки

Windows, Python 3.12.10:

| Проверка | Результат |
| --- | --- |
| `python -B tests/validate_manifest.py` | OK, 40 компонентов |
| `python -B -m unittest discover -s design/tests -v` с writable TMP/TEMP | 19/19; все 30 навыков устанавливаются во все три одноразовых runtime homes с совпадающими SHA-256; dry-run не пишет файлы |
| `python -B -m unittest discover -s tests -v` вне sandbox | 10/10 без пропусков, включая PowerShell wrapper, Windows junction/8.3 и текущие файлы/историю Git на очевидные секреты |
| `skill-creator/scripts/quick_validate.py`, функция `validate_skill` для каждого навыка | 30/30; использована уже установленная PyYAML из окружения SkillSpector, новые зависимости не устанавливались |
| Исходные хеши против lock коммита 9c6c604 | Все 85 исходных хешей сохранены; изменены ровно 29 SKILL.md, остальные 56 файлов совпадают |
| Ссылки основного README, design README и Cloud guide | Локальные targets существуют |
| SkillSpector 2.12.0, `scan --recursive --no-llm` | 29/29, максимум LOW 20/100; HIGH/CRITICAL отсутствуют; все срабатывания прочитаны вручную |
| Нативный PowerShell preview для Hermes | `impeccable-design` и `design-taste-frontend`: exit 0, два DRY-RUN, без установки в профиль |
| Git index / финальный diff | SHA-256 всех 90 locked skill-файлов совпадают; `git diff --cached --check` проходит; Git распознаёт 85 переносов |

Обычный preview не включает optional-навыки. Общий manual routing отказывается применяться во всех трёх runtime. Hermes-only operator остаётся недоступен другим runtime.

## Границы доказательств

Проверена установка файлов; native discovery, соблюдение инструкций моделью, наличие инструментов генерации/браузера/устройства и фактическая работа в Codex Cloud не проверялись. Новые `tested_on` остаются пустыми. Статический анализ частичный: 11 полных и 18 частичных skill-анализов, заявленное покрытие 37.93%. Качество дизайна, экономия токенов и реальный Jev не измерялись. Подробности — [shared-runtime-review.md](provenance/shared-runtime-review.md).
