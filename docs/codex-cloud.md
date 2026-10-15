# Продолжить agent-stack в Codex Cloud

Проверено по официальной документации OpenAI 15 октября 2026 года. Состояние конкретного аккаунта и запуск этого репозитория в Cloud в этой локальной работе не проверялись.

## Создать окружение

В новой задаче выбери **Work in → Cloud → Select environment → Create environment**, подключи `typakon4/agent-stack`, проверь отчёт подготовки и нажми **Publish**. Затем выбери **Start a new task**. Альтернативный вход: **Settings → Codex Cloud → Environments → Create environment**. [Официальная инструкция](https://learn.chatgpt.com/docs/environments/cloud-environments).

Попроси использовать актуальный `master`, существующий Python 3.12+ и выполнить команды ниже. Сторонние Python-зависимости этому репозиторию не нужны:

```sh
git status --short --branch
git log -1 --oneline
python -B tests/validate_manifest.py
python -B -m unittest discover -s tests -v
python -B -m unittest discover -s design/tests -v
```

## Что передать агенту

Вставь в облачную задачу:

```text
Продолжаем работу над typakon4/agent-stack с актуального master.
Прочитай README.md, design/README.md, docs/compatibility.md,
shared/instructions/design-routing.md и design/VERIFICATION.md.
Проверь git status, текущий commit, manifest и оба набора unittest.

В shared/skills находятся 30 общих дизайн-навыков для Hermes/OMP/Codex.
Они optional; original/current SHA-256 сохранены в design/source-lock.json.
Общие targets и тест копирования не доказывают native discovery или model adherence.
Сохрани явный вызов prototype, pick-ui-library и review-animations.
Impeccable остаётся статическим, без engine/hooks/live server.
Jev concept selection — офлайн-контракт, реальный адаптер не подключён.

Сохраняй текущую архитектуру и явные ограничения installer.
Не переноси secrets, профили, raw chats и локальные MCP-настройки.
Не устанавливай зависимости, не публикуй, не делай commit/push без моего разрешения.
Если для следующего задания нужен skill, прочитай только подходящий SKILL.md
и нужные references из shared/skills. Затем продолжай мою следующую задачу.
```

Это краткая передача решений и ссылок на файлы. Она не является импортом всей истории локального чата.

## Навыки в окружении

`shared/skills` — каталог исходников agent-stack; сам по себе этот путь не является штатным каталогом автоматического обнаружения Codex. Можно явно дать агенту нужный `SKILL.md`, как в тексте выше.

Если требуется каталог навыков, Codex документирует `$HOME/.agents/skills` для пользовательской установки и `.agents/skills` внутри репозитория для проектной. Наш installer сохраняет запрет установки внутрь собственного checkout; для него используй отдельный пользовательский корень. [Расположение skills](https://learn.chatgpt.com/docs/build-skills).

Пример предпросмотра в Linux Cloud из корня agent-stack:

```sh
mkdir -p "$HOME/.agents"
python installers/install.py codex \
  --component design-reference-loop \
  --component design-taste-frontend \
  --component emil-design-eng \
  --component impeccable-design \
  --destination "$HOME/.agents" --no-clobber --dry-run
```

После разрешения на выбранные компоненты замени `--dry-run` на `--apply`. Проверь обнаружение навыков в самом Cloud; наличие файлов его не доказывает. Routing объединяется с инструкциями отдельно и вручную. Не создавай второй одноимённый каталог, если выбранный навык уже доступен из плагина или другого root.

## Что остаётся локально

Личные skills с ПК не синхронизируются автоматически. Cloud использует собственные файлы и сервисы; локальные процессы, браузерные входы и VPN туда автоматически не передаются. По текущей документации browser/computer use в Cloud пока не поддерживаются. Задачи с такой проверкой оставляй локально либо явно отмечай непроверенную часть. [Cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments), [режимы выполнения](https://learn.chatgpt.com/docs/environments/modes).

Изменения текущей Cloud-задачи не обновляют стартовую среду будущих задач: для изменения reusable setup нужно отредактировать и повторно опубликовать environment. Исходный код передаётся через Git, публикация окружения не заменяет сохранение кода в репозитории. [Состояние окружений](https://learn.chatgpt.com/docs/environments/cloud-environments).
