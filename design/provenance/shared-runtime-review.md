# Review общей адаптации — 2026-10-15

Пользователь запросил общие targets для дизайн-стека. Источники и лицензии не обновлялись; основа — рассмотренный импорт коммита `9c6c604`. [Первичный review](security-review.md) относится к исходной Codex-ревизии.

Изменены только 29 SKILL.md: интеграционный заголовок, граница возможностей и разрешений выбранного host; у `image-to-code` нейтрализовано название host в описании. Codex-specific подсказки остаются условными. Общая библиотека не предоставляет imagegen/browser/device/subagents; их отсутствие обозначается явно. Подключение сервисов, смена провайдера и запуск subagents без поддержки и разрешения не допускаются. Явный вызов трёх специализированных навыков сохранён в тексте и Codex metadata. Routing переведён в общий manual fragment.

Исходные и текущие хеши закреплены в `source-lock.json`. Лицензии, ресурсы и metadata — 56 файлов — сохранились байт в байт. Никаких executable, hooks, setup scripts, MCP или live server в payload не добавлено. Установщик и его allowlist не изменены. Активные профили не затронуты.

## Скан и ручной разбор

Pinned SkillSpector 2.12.0, `scan --recursive --no-llm`. Отчёт сохранён вне репозитория. Просканированы 29 навыков, пропусков нет. Максимальный score — 20/100 LOW, рекомендация CAUTION, HIGH/CRITICAL отсутствуют. Анализ частичный: 11 полных и 18 частичных результатов, заявленное покрытие 37.93%; ограничения parser/reference resolution остаются.

Проверены все отмеченные места в текущих файлах:

- `animate-expo/RECIPES.md:10,258`, `animate-expo/SKILL.md:91,217`: примеры установки Expo-зависимостей, требующие отдельного разрешения и совместимых версий.
- `animate-expo/SKILL.md:227`: пример iOS frame-rate infoPlist; без выполнения или изменений host.
- `design-taste-frontend/SKILL.md:58`, `design-taste-frontend-v1/SKILL.md:20`, `imagegen-frontend-web/SKILL.md:106`: conversational override стиля, без отмены разрешений.
- `design-taste-frontend/SKILL.md:106,1035,1036`: примеры shadcn, включая `@latest`; текст примера не разрешает установку или выбор версии.
- `imagegen-frontend-mobile/SKILL.md:77`: substring `plist` в слове `simplistic`.
- `impeccable-design/references/audit.md:138`: запрет ложных результатов без проверки; `LICENSE:56` — формулировка Apache license.

Решение: **safe to consider** в разрешённом пользователем объёме общих статических инструкций и выборочной установки. Native discovery и поведение каждого runtime не подтверждены. Повторный static scan и тесты копирования не являются независимой поведенческой оценкой.
