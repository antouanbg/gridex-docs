# Чернова за одобрение: услуги, заявки и достъпи / DRAFT: service requests and grants

**Статус към 2026-10-01:** само предложение. Потребителският екран не се променя.
Новите административни списъци, отмяната на заявка, предложенията и имейлите
**не са одобрени като цял процес и не са обявени за внедрени**. Този документ е
извън публичното меню на Docusaurus. След като собственикът потвърди логиката
и трите екрана, се започва код, тестове и чак тогава публична BG/EN помощ.

## Български

### Източник на самоличност и данни

- OpenRemote/Keycloak удостоверява realm и subject. GrideX API определя
  действителната роля от текущото членство и изрично разрешения platform
  subject; frontend получава резултата чрез `/api/v1/me`. Бутон или скрита
  секция не е защита — API повтаря проверката за всяко действие.
- Вече съществуват PostgreSQL таблици `organisation_memberships`,
  `service_catalog`, `organisation_services`, `member_services`,
  `organisation_market_zones`, `service_requests` и
  `service_request_events`. TimescaleDB пази пазарни и телеметрични данни,
  не роли и одобрения. Наличните таблици за заявки не съдържат пълна логика
  за „предложение/покана“ или „отменена заявка“.
- Предложение: всяка нова покана, заявка, промяна на статус, решение,
  получател, актьор и час да има траен запис и одит в backend PostgreSQL.
  Списъците се четат със server-side странициране и филтриране, без лимит
  на общия брой и без изтегляне на всички организации към клиентски браузър.

### Предложен поток

```mermaid
flowchart TD
  U[Потребител заявява услуга] --> O[Админът на неговата организация вижда заявката]
  O --> G{Организацията има ли разрешение?}
  G -- Да --> M{Админът решава за потребителя}
  G -- Не --> P[Само админът на организацията заявява към супер админ]
  P --> W[Чака решение; само заявилият админ може да отмени]
  W --> S{Супер админ одобрява или отказва}
  S -- Одобрява --> Z[Услуга за организация + отделна BG зона при цени]
  Z --> M
  S -- Отказва --> R[Статус и уведомление; без достъп]
  M -- Одобрява --> A[Лично право за точния потребител]
  M -- Отказва --> R
```

Супер администраторът може и да започне предложение за услуга към активна
организация. Администраторът на организацията може да започне предложение
към свой одобрен потребител **само за услуга, разрешена на организацията**.
Дали тези предложения изискват изрично приемане от получателя или са пряко
администраторско разрешение остава **отворено решение на собственика**.
Нито заявка, нито предложение само по себе си дава достъп. Отнемането на
организационно право каскадно спира личните права; повторното разрешаване не
ги възстановява автоматично.

### Три екрана — предложена редакция за одобрение

Няма избор на роля в работещия сайт. Трите екрана се показват един до друг
само в прегледа; реалният потребител вижда единствено екрана, позволен от
backend правата му.

1. **Супер администратор** — съществуващият
   „Клиенти и договори → Потребители и покани → Услуги“:
   избор на активна организация; ред за всяка услуга и BG зона; отделни
   списъци „Поканени организации и чакащи решения“ и „Одобрени организации
   и услуги“. Ред: организация, услуга/зона, статус, изпратена/решена на,
   допустимо действие. Търсене, статус филтър и странициране. Спряната
   организация е само за преглед.
2. **Администратор на организация** — същият съществуващ раздел, само за
   собствената организация. В „Услуги за организацията“ всяка неразрешена
   заявяема услуга има **„Заяви“**; при чакаща заявка бутонът става
   **„Отмени заявката“**, достъпен само за администратора. Отделни списъци
   „Поканени потребители и техните заявки“ и „Одобрени потребители и
   услуги“, с търсене, статус и странициране. Одобрение за организация не
   включва автоматично никой потребител.
3. **Потребител** — съществуващият предложен „Профил → Услуги“ остава
   **без промяна**: личен каталог, бутон „Заяви“ за заявяемите услуги и
   личен статус. Няма административни списъци, избор на организация или
   администраторски действия.

```text
СУПЕР АДМИН  Клиенти и договори / Потребители и покани / Услуги
  [Избери одобрена организация]   [Услуги и BG зона: разреши/откажи/отнеми]
  Поканени организации и чакащи решения   [Търси] [Статус]
  Организация | Услуга | Статус | Дата | Действие       [Назад] 1/N [Напред]
  Одобрени организации и услуги           [Търси]
  Организация | Услуга | Статус | Решена на         [Назад] 1/N [Напред]

АДМИН НА ОРГАНИЗАЦИЯ  Клиенти и договори / Потребители и покани / Услуги
  Услуги за организацията: [Заяви] → [Чака решение] [Отмени заявката]
  Поканени потребители и техните заявки   [Търси] [Статус]
  Потребител | Услуга | Статус | Дата | Действие       [Назад] 1/N [Напред]
  Одобрени потребители и услуги           [Търси]
  Потребител | Услуга | Статус | Решена на         [Назад] 1/N [Напред]

ПОТРЕБИТЕЛ  Профил / Услуги — без промяна
  Личен каталог: [Заяви] / [Чака решение] / [Предстои]
```

Всички списъци са за произволен брой записи. Desktop показва редове; mobile
ги подрежда вертикално без хоризонтално скролиране. При празен резултат се
показва „Няма записи“, а при грешка — съобщение с безопасен повторен опит.
След запис екранът показва потвърден от API резултат; не приема непотвърдено
изпращане за успех.

### Задължителни проверки преди внедряване

- Изрично одобрение от собственика на този поток и на ревизираните три
  екрана, включително на поведението на предложенията.
- Backend миграция само за липсващите състояния/събития и pagination,
  без изтриване или пренаписване на съществуващи заявки и разрешения.
- Тестове за роли, cross-realm отказ, много записи, филтри, отмяна,
  двойно натискане, имейл без дублиране, отнемане и безопасно възстановяване.
- След реално внедряване: BG/EN публична помощ в Docusaurus и връзка
  „Помощ“ от всеки засегнат екран. Преди това тази чернова не влиза в
  публичната навигация.

## English

**Status:** proposal only. The member screen stays unchanged. The revised
admin lists, request cancellation, offers and email behavior are not yet
approved as one workflow or claimed live.

OpenRemote/Keycloak authenticates the realm and subject; the GrideX API derives
the actual role from current membership and the explicitly allowed platform
subject. The API, not a hidden frontend control, authorizes every action.
Organisation roles, grants, requests and events live in GrideX PostgreSQL;
TimescaleDB stores market and telemetry series, not these rights. Offers and
cancellation need new backend states/events after approval. All invitations,
requests, decisions, actors and timestamps must persist and remain auditable.
Lists use server-side pagination and filtering for any number of records.

The member requests a service from their organisation administrator. If the
organisation lacks it, only that administrator may request it from the
platform administrator and cancel their pending request. The platform
administrator approves or rejects the organisation grant and separately the
BG market zone where applicable. The organisation administrator then decides
the member grant. No request grants access. Revoking an organisation grant
stops member grants; re-granting does not silently restore them. Platform-
initiated organisation offers and organisation-admin-initiated member offers
are proposed, but whether recipient acceptance is mandatory remains an
explicit owner decision.

**Screens:** platform admin sees one selected active organisation, its
service/zone controls, a paginated searchable list of invitations/pending
decisions and a separate list of approved organisation grants. Organisation
admin sees only their organisation, Request/Cancel on unapproved requestable
service rows, a list of invited/pending members and a separate list of
approved member grants. Member sees the existing personal service catalog
unchanged, with no administration lists. The real site never exposes a
role-switching control; it renders the one verified role. Mobile stacks rows
without horizontal overflow. Empty, error, retry and confirmed-success states
must be documented. After owner approval, implement and test; only then
publish BG/EN live Docusaurus help and link it from affected screens.
