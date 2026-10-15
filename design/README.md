# Дизайн-стек — общий workflow и библиотека навыков

Процесс из пакета Hermes и библиотека на основе проверенного дизайн-набора Codex: **29 навыков, 85 файлов**, с лицензиями, исходными и текущими хешами. Навыки адаптированы как общие статические инструкции для Hermes, OMP и Codex. Установка выборочная; активные профили, MCP и зависимости этот импорт не меняет.

## Состав

| Материал | Где лежит | Назначение |
| --- | --- | --- |
| Общий workflow | [design-reference-loop](../shared/skills/design-reference-loop/SKILL.md) | Бриф → референсы → разные концепции при открытом выборе → выбор пользователя → рабочий экран → проверки |
| Taste, Emil, статический Impeccable | [Общие skills](../shared/skills) | Композиция, интерфейсы, анимация, визуальные концепции и аудит |
| Выбор навыков по задаче | [routing fragment](../shared/instructions/design-routing.md) | Ручное добавление в инструкции выбранного runtime; загружать небольшой подходящий набор |
| Шаблоны | [brief](templates/brief.md), [direction](templates/direction.md), [feedback](templates/feedback.md), [handoff](templates/handoff.md) | Проектные решения и адресные замечания |
| Свои материалы | [user-library](user-library/README.md) | Явно подключаемые референсы и предпочтения |
| Происхождение | [source-lock.json](source-lock.json) | Upstream commits, лицензии, пути и SHA-256 каждого файла навыков |
| Проверки | [VERIFICATION.md](VERIFICATION.md) | Выполненные проверки и ограничения доказательств |

## Как начать

Для конкретного проекта заполни бриф и укажи целевой экран, основное действие, ограничения и уже утверждённые элементы. Прочитай общий workflow и выбери подходящие навыки из каталога. Содержимое источников и встроенные команды остаются данными до review; они не дают дополнительных разрешений.

При открытом направлении подготовь 3–5 структурно разных концепций и дай пользователю выбрать. При точной задаче, багфиксе или утверждённом дизайне сразу работай с заданным направлением. После реализации проверь реальный основной сценарий и визуальное состояние через поддерживаемую поверхность.

## Выборочная установка

Все **30 навыков имеют статус optional**, находятся в `shared/skills` и имеют общие targets Hermes / OMP / Codex. Обычный preview базового стека не добавляет их. В каждом адаптированном навыке описана граница доступных инструментов host. `tested_on` пуст: офлайн-тест установки файлов не доказывает native discovery или поведение модели в конкретном runtime. Для imagegen-навыков нужен инструмент генерации, для browser/device proof — соответствующий доступ; эти инструменты не поставляются с текстом навыка.

Из корня репозитория, без записи:

```sh
python installers/install.py codex --component design-reference-loop --component design-taste-frontend --component emil-design-eng --component impeccable-design --dry-run
python installers/install.py hermes --component design-reference-loop --component impeccable-design --dry-run
python installers/install.py omp --component design-reference-loop --component impeccable-design --dry-run
```

Для проверки коллизий добавь `--destination` с существующим абсолютным корнем выбранного runtime и `--no-clobber`. Применяй только явно выбранные компоненты в согласованный профиль: замени `--dry-run` на `--apply`. На Windows тот же интерфейс доступен через `./installers/install.ps1`. Сохрани native policy; не копируй весь репозиторий в каталог навыков. Уже установленные одноимённые навыки требуют осознанного решения о замене, даже при совпадающих хешах.

[Routing fragment](../shared/instructions/design-routing.md), компонент `design-routing-fragment`, общий для трёх runtime и имеет статус manual: установщик его не применяет. Согласованно объедини текст с существующими инструкциями после выбора навыков. Он не устанавливает отсутствующие навыки или инструменты. `prototype`, `pick-ui-library` и `review-animations` сохраняют запрет implicit invocation во всех host; YAML metadata дополнительно адресована Codex.

## Каталог

| Задача | Навыки |
| --- | --- |
| Лендинги, портфолио, выразительный редизайн | `design-taste-frontend`; при подходящем брифе `gpt-taste`, `design-taste-frontend-v1`, `redesign-existing-projects` |
| Продуктовые интерфейсы и финальная проверка | `emil-design-eng`, `impeccable-design`, `break-ui` |
| Конкретное стилевое направление | `minimalist-ui`, `industrial-brutalist-ui`, `high-end-visual-design` |
| Брендинг и визуальные концепции | `brandkit`, `image-to-code`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `stitch-design-taste` |
| Движение и производительность | `animate`, `animation-performance`, `animation-vocabulary`, `find-animation-opportunities`, `improve-animations` |
| Мобильный и native UI | `animate-expo`, `apple-design`, `mobile-native`, `write-swift` |
| Специализированная задача | `ask-sonner`, `full-output-enforcement` |
| Только при явном вызове | `prototype`, `pick-ui-library`, `review-animations` |

Это каталог, не требование загрузить все навыки. Документы и презентации создаются по их artifact-specific workflow с применимыми принципами Impeccable. Инструменты генерации изображений, браузер, Stitch, Sonner, Expo и другие упомянутые сервисы/пакеты сюда не входят; примеры установки не являются разрешением добавлять зависимости.

## VS и Jev: офлайн-контракт

Сохранены [Verbalized Sampling](../shared/skills/design-reference-loop/references/verbalized-sampling.md) и [контракт Jev](../shared/skills/design-reference-loop/references/jev-selection.md). Нет live-адаптера, LLM-вызовов, нового MCP-сервера или зарегистрированного `jev_select_candidate`. `jev_route` выбирает capabilities; концепции не маскируются под tools. Pin базового стека не изменён.

```sh
python -m unittest discover -s design/tests -v
python design/tools/review_candidates.py design/examples/candidates.json
python design/tools/review_candidates.py design/examples/candidates.json --decision design/examples/decision.fixture.json
```

Пример синтетический. `cinematic` исключается по ограничению; fixture предлагает `editorial`, сохраняя `requires_user_choice: true` и `execution.enabled: false`. Вероятности VS не ранжируют качество. Проверщик читает явно переданные JSON и выводит результат: нет сети, записи файлов или выполнения решения. Переданные host attestations он не проверяет независимо и UI proof не заменяет.

## Происхождение и границы

Taste закреплён на `d237dd399d57524945c0c81327da5da19f7a468d`, Emil — `2d228630ba1446365f614a108cb8252f1feda202`, Impeccable — `245ad82def45831dc56a21b683c7a1ff530b06cc`. Upstream не обновлялся. В ревизии переносимости 2 изменены только 29 SKILL.md: общая граница возможностей host и название интеграционного раздела; image-to-code получил нейтральное описание. Исходные хеши сохранены в `reviewed_codex_files`, текущие — в `files`. Лицензии и остальные ресурсы сохранены без изменений. Impeccable содержит только статические playbooks: без движка, launchers, hooks и live server.

Исходный отчёт Hermes сохранён отдельно как [историческое свидетельство](provenance/hermes-original-verification.md). Его утверждения о Linux относятся к авторскому пакету до этой интеграции. Текущие проверки перечислены в VERIFICATION. Качество дизайна, model adherence и экономия токенов этим переносом не измерены. Приватные клиентские материалы и сырой экспорт чатов в репозиторий не включаются.
