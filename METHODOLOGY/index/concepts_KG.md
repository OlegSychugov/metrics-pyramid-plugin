<KnowledgeGraph>
  <Пирамида_метрик>
    <keywords>пирамида метрик:9|иерархия метрик:8|бизнес-цели:7|клиентоцентричность:8|декомпозиция:9</keywords>
    <terms>Metrics Pyramid|Product Metrics|Decomposition|Hierarchy of Metrics</terms>
    <annotation>Иерархическая модель для организации и декомпозиции продуктовых метрик. Она выстраивает показатели от верхнеуровневых бизнес-целей до конкретных метрик качества продукта, обеспечивая связь между действиями команды и результатами компании, а также поддерживая клиентоцентричный подход.</annotation>

    <Особенности_пирамиды_метрик_продукта TYPE="HAS_CHARACTERISTIC">
      <keywords>интеграция:8|клиентоцентричность:9|учет рисков:7|декомпозиция:9</keywords>
      <terms>Features|Principles|Product metrics pyramid specifics</terms>
      <annotation>Ключевые принципы, лежащие в основе пирамиды метрик, которые делают ее эффективным инструментом управления продуктом.</annotation>

      <Интеграция_полярных_смыслов TYPE="IS_PART_OF">
        <keywords>бизнес-цели:8|цели пользователей:8|интеграция:9|баланс:7</keywords>
        <terms>Integration of goals|Business vs User needs</terms>
        <annotation>Особенность пирамиды, заключающаяся в объединении и балансировке целей бизнеса (ЛПР, компания, процессы) и целей пользователей/клиентов в единой системе метрик.</annotation>
      </Интеграция_полярных_смыслов>

      <Клиентоцентричность TYPE="IS_PART_OF">
        <keywords>акцент на клиента:9|пользовательский опыт:8|ценность для клиента:9</keywords>
        <terms>Customer-centricity|User focus</terms>
        <annotation>Фундаментальный принцип пирамиды, согласно которому метрики нижних уровней (ценность, качество) сфокусированы на решении проблем и удовлетворении потребностей клиента, что в итоге приводит к росту верхнеуровневых бизнес-метрик.</annotation>
        <CrossLinks>
          <Link TARGET="Уровень_Ценности" TYPE="IS_MANIFESTATION_OF" RELEVANCE="9"/>
          <Link TARGET="Уровень_Качества" TYPE="IS_MANIFESTATION_OF" RELEVANCE="9"/>
        </CrossLinks>
      </Клиентоцентричность>

      <Учет_рисков_через_иерархию TYPE="IS_PART_OF">
        <keywords>риски:8|накрутка метрик:7|иерархия:9|снизу-вверх:6</keywords>
        <terms>Risk management|Metric gaming|Hierarchy rule</terms>
        <annotation>Принцип, согласно которому инициативы не должны выходить в продакшн, если они улучшают метрики нижнего уровня (например, качество), но негативно влияют на метрики верхнего уровня (например, маржинальность или лояльность). Это предотвращает "накрутку" локальных показателей в ущерб общей цели.</annotation>
      </Учет_рисков_через_иерархию>

      <Декомпозиция_верхних_метрик_на_нижние TYPE="IS_PART_OF">
        <keywords>декомпозиция:9|сверху-вниз:7|прокси-метрики:8|стратегия:8</keywords>
        <terms>Decomposition|Top-down approach|Proxy metrics</terms>
        <annotation>Процесс разбиения высокоуровневых метрик (например, Revenue) на более конкретные и управляемые метрики нижних уровней (лояльность, ценность, качество). Это позволяет команде понять, на какие именно рычаги нужно влиять для достижения стратегических целей.</annotation>
      </Декомпозиция_верхних_метрик_на_нижние>
    </Особенности_пирамиды_метрик_продукта>

    <Уровень_Бизнеса TYPE="IS_LEVEL_OF">
      <keywords>бизнес-метрики:9|Revenue:8|MAU:7|инвесторы:7|амбиции фаундера:6</keywords>
      <terms>Business Metrics|Top Level Metrics|Vanity Metrics</terms>
      <annotation>Верхний уровень пирамиды, отражающий самые главные цели компании. Эти метрики важны для основателей, инвесторов и высшего руководства. Они показывают общее здоровье и масштаб бизнеса.</annotation>

      <Валовые_показатели TYPE="IS_EXAMPLE_OF">
        <keywords>Revenue:9|MAU:8|Выручка:9|Активная аудитория:8</keywords>
        <terms>Gross metrics|Revenue|MAU (Monthly Active Users)</terms>
        <annotation>Ключевые финансовые и аудиторные показатели, такие как общая выручка (Revenue) и количество уникальных активных пользователей в месяц (MAU).</annotation>
      </Валовые_показатели>

      <Нефинансовые_показатели TYPE="IS_EXAMPLE_OF">
        <keywords>монетизация:7|аудитория:8|потенциал:7|Telegram:5</keywords>
        <terms>Non-financial metrics|Pre-monetization metrics</terms>
        <annotation>Метрики, которые важны для продуктов на ранней стадии, когда модель монетизации еще не определена. Часто это показатели роста аудитории и ее вовлеченности, на которые смотрят инвесторы.</annotation>
      </Нефинансовые_показатели>

      <Личные_амбиции_фаундера TYPE="IS_FACTOR_OF">
        <keywords>фаундер:9|миссия:8|видение:8|драйвер:7</keywords>
        <terms>Founder's ambitions|Mission-driven metrics</terms>
        <annotation>Часто ключевая бизнес-метрика является отражением личной миссии или амбиций основателя компании. Важно понимать этот драйвер, так как он определяет стратегическое направление развития продукта.</annotation>
        <CrossLinks>
          <Link TARGET="NSM_North_Star_Metric" TYPE="INFLUENCES" RELEVANCE="8"/>
        </CrossLinks>
      </Личные_амбиции_фаундера>
    </Уровень_Бизнеса>

    <Уровень_Маржинальности TYPE="IS_LEVEL_OF">
      <keywords>маржинальность:9|юнит-экономика:9|LTV:8|CAC:8|OPEX:7|ARPU:7</keywords>
      <terms>Margin Level|Unit Economics|Profitability Metrics</terms>
      <annotation>Второй уровень пирамиды, декомпозирующий бизнес-метрики на показатели, связанные с прибыльностью в расчете на одного клиента (юнита). Показывает экономическое здоровье продукта.</annotation>
      <CrossLinks>
        <Link TARGET="Уровень_Бизнеса" TYPE="IS_DECOMPOSITION_OF" RELEVANCE="9"/>
      </CrossLinks>

      <Юнит_экономика TYPE="IS_FORMULA_OF">
        <keywords>LTV:9|CAC:9|OPEX:8|прибыльность на клиента:9</keywords>
        <terms>Unit Economics|LTV - CAC - OPEX</terms>
        <annotation>Формула расчета прибыльности продукта на одного пользователя: LTV (пожизненная ценность клиента) минус CAC (стоимость привлечения клиента) минус OPEX (операционные расходы на клиента).</annotation>
      </Юнит_экономика>

      <LTV_Lifetime_Value TYPE="IS_PART_OF">
        <keywords>пожизненная ценность:9|когорты:8|доход с клиента:9|gross маржа:7</keywords>
        <terms>LTV|Lifetime Value|Customer Lifetime Value</terms>
        <annotation>Общая прибыль, которую компания получает от одного клиента за все время его взаимодействия с продуктом. Рассчитывается по когортам и может быть фактическим или прогнозным.</annotation>
        <CrossLinks>
          <Link TARGET="Retention" TYPE="IS_RELATED_TO" RELEVANCE="9"/>
        </CrossLinks>
      </LTV_Lifetime_Value>

      <CAC_Customer_Acquisition_Cost TYPE="IS_PART_OF">
        <keywords>стоимость привлечения:9|маркетинг:8|затраты на привлечение:9</keywords>
        <terms>CAC|Customer Acquisition Cost</terms>
        <annotation>Сумма всех затрат на маркетинг и продажи, деленная на количество привлеченных за этот период клиентов. Показывает, во сколько обходится компании один новый клиент.</annotation>
      </CAC_Customer_Acquisition_Cost>

      <ARPU_Average_Revenue_Per_User TYPE="IS_PART_OF">
        <keywords>средний чек:8|доход на пользователя:9|ARPU:9</keywords>
        <terms>ARPU|Average Revenue Per User</terms>
        <annotation>Средний доход, приносимый одним активным пользователем за определенный период. Рассчитывается как общий доход, деленный на общее число активных пользователей.</annotation>
      </ARPU_Average_Revenue_Per_User>

      <ARPPU_Average_Revenue_Per_Paying_User TYPE="IS_PART_OF">
        <keywords>средний чек платящего:9|ARPPU:9|доход на платящего:9</keywords>
        <terms>ARPPU|Average Revenue Per Paying User</terms>
        <annotation>Средний доход, приносимый одним платящим пользователем за определенный период. Этот показатель помогает понять ценность для тех, кто платит.</annotation>
      </ARPPU_Average_Revenue_Per_Paying_User>

    </Уровень_Маржинальности>

    <Уровень_Лояльности TYPE="IS_LEVEL_OF">
      <keywords>лояльность:9|возвращаемость:8|виральность:7|retention:9|churn:8</keywords>
      <terms>Loyalty Level|Retention Metrics|Virality</terms>
      <annotation>Третий уровень, декомпозирующий маржинальность. Отражает степень приверженности клиентов продукту. Лояльность состоит из двух ключевых компонентов: возвращаемость (клиент продолжает пользоваться продуктом) и референтность (клиент рекомендует продукт другим).</annotation>
      <CrossLinks>
        <Link TARGET="Уровень_Маржинальности" TYPE="IS_DECOMPOSITION_OF" RELEVANCE="9"/>
      </CrossLinks>

      <Retention TYPE="IS_METRIC_OF">
        <keywords>retention:9|возвращаемость:9|удержание:8|когорты:8</keywords>
        <terms>Retention Rate|User Retention</terms>
        <annotation>Процент пользователей, которые вернулись к использованию продукта через определенное время после первого взаимодействия. Считается по когортам и является ключевым предсказателем долгосрочной оплаты и LTV.</annotation>
      </Retention>

      <Churn_Rate TYPE="IS_METRIC_OF">
        <keywords>отток:9|churn:9|потеря клиентов:8</keywords>
        <terms>Churn Rate|Attrition Rate</terms>
        <annotation>Процент пользователей, которые прекратили использовать продукт за определенный период. Показывает "дыру в ведре", которую необходимо минимизировать.</annotation>
      </Churn_Rate>

      <NPS_Net_Promoter_Score TYPE="IS_METRIC_OF">
        <keywords>NPS:9|индекс лояльности:8|рекомендации:9|промоутеры:7|детракторы:7</keywords>
        <terms>NPS|Net Promoter Score</terms>
        <annotation>Метрика, измеряющая готовность клиентов рекомендовать продукт или компанию. Рассчитывается на основе опроса "С какой вероятностью вы порекомендуете наш продукт друзьям?".</annotation>
      </NPS_Net_Promoter_Score>

      <Key_Factor TYPE="IS_METRIC_OF">
        <keywords>виральность:8|реферальная ссылка:7|сарафанное радио:7</keywords>
        <terms>K-factor|Virality Coefficient</terms>
        <annotation>Показатель виральности продукта; показывает, сколько новых пользователей приводит один существующий пользователь (например, через реферальные ссылки).</annotation>
      </Key_Factor>

      <Sticky_Factor TYPE="IS_METRIC_OF">
        <keywords>прилипание:8|DAU_slash_MAU:9|вовлеченность:8|stickiness:9</keywords>
        <terms>Stickiness|Sticky Factor|DAU/MAU Ratio</terms>
        <annotation>Метрика, показывающая, насколько регулярно пользователи возвращаются в продукт в течение месяца. Рассчитывается как отношение дневной активной аудитории (DAU) к месячной (MAU).</annotation>
      </Sticky_Factor>

      <Возврат_во_вторую_покупку_C2 TYPE="IS_METRIC_OF">
        <keywords>вторая покупка:8|C2:8|продление подписки:7|повторная продажа:8</keywords>
        <terms>Repeat Purchase Rate|C2 Conversion</terms>
        <annotation>Метрика, отслеживающая конверсию в повторную покупку или продление подписки. Отличается от Retention, который измеряет использование, а не оплату. Управление использованием (Retention) помогает предсказывать и влиять на C2.</annotation>
        <CrossLinks>
          <Link TARGET="Retention" TYPE="IS_DIFFERENT_FROM" RELEVANCE="8"/>
        </CrossLinks>
      </Возврат_во_вторую_покупку_C2>

    </Уровень_Лояльности>

    <Уровень_Ценности TYPE="IS_LEVEL_OF">
      <keywords>ценность:9|NSM:9|PVM:8|решение проблемы:9|job-to-be-done:7</keywords>
      <terms>Value Level|Product Value Metrics (PVM)|North Star Metric (NSM)</terms>
      <annotation>Четвертый, клиентоцентричный уровень пирамиды. Отражает, насколько хорошо продукт решает основную проблему пользователя (Main Job). Фокусировка на метриках ценности запускает "магию сложного процента", приводя к росту лояльности и, как следствие, бизнес-показателей.</annotation>
      <CrossLinks>
        <Link TARGET="Уровень_Лояльности" TYPE="IS_DECOMPOSITION_OF" RELEVANCE="9"/>
      </CrossLinks>

      <NSM_North_Star_Metric TYPE="IS_SUBTYPE_OF">
        <keywords>NSM:9|North Star Metric:9|путеводная звезда:8|ключевая ценность:9</keywords>
        <terms>NSM|North Star Metric|OMTM</terms>
        <annotation>Единственная метрика, которая наилучшим образом отражает ключевую ценность, доставляемую продуктом клиентам. Она служит ориентиром для всей команды. NSM может отражать как ценность для клиента, так и миссию фаундера.</annotation>
      </NSM_North_Star_Metric>
      
      <Примеры_метрик_ценности TYPE="PROVIDES_EXAMPLE_FOR">
        <keywords>скорость подачи:8|время ожидания:8|экономия времени:9|экономия денег:9|количество действий:7</keywords>
        <terms>Time-to-value|Time saved|Money saved|Number of clicks</terms>
        <annotation>Метрики ценности уникальны для каждого продукта и часто связаны с экономией или накоплением ресурсов (время, деньги), либо с уменьшением усилий пользователя. Например, для Uber это скорость и точность подачи машины.</annotation>
      </Примеры_метрик_ценности>
    </Уровень_Ценности>

    <Уровень_Качества TYPE="IS_LEVEL_OF">
      <keywords>качество:9|PQM:8|баги:7|недоступность:7|помогает_vs_мешает:9</keywords>
      <terms>Quality Level|Product Quality Metrics (PQM)|User Friction</terms>
      <annotation>Самый нижний и детальный уровень пирамиды, декомпозирующий ценность. Метрики качества отвечают на два вопроса: "Что помогает пользователю решить свою проблему в продукте?" и "Что мешает ему это сделать?". Часто метрики качества — это бывшие метрики ценности, которые стали отраслевым стандартом.</annotation>
      <CrossLinks>
        <Link TARGET="Уровень_Ценности" TYPE="IS_DECOMPOSITION_OF" RELEVANCE="9"/>
        <Link TARGET="Уровень_Ценности" TYPE="EVOLVES_INTO" RELEVANCE="6"/>
      </CrossLinks>

      <Метрики_помогающие_пользователю TYPE="IS_SUBTYPE_OF">
        <keywords>помощь:8|успешный сценарий:7|завершение цикла:7|понятные инструкции:6</keywords>
        <terms>Success metrics|Enablers</terms>
        <annotation>Показатели, отражающие факторы, которые способствуют успешному решению задачи пользователя. Например, процент завершенных ключевых сценариев, использование подсказок.</annotation>
      </Метрики_помогающие_пользователю>

      <Метрики_мешающие_пользователю TYPE="IS_SUBTYPE_OF">
        <keywords>баги:8|ошибки:8|недоступность сервиса:8|трение:7|краши:7</keywords>
        <terms>Friction metrics|Blockers|Bugs|Errors</terms>
        <annotation>Показатели, отражающие проблемы и барьеры на пути пользователя. К ним относятся количество багов на сессию, процент пользователей, столкнувшихся с критической ошибкой, время недоступности сервиса, галлюцинации нейросети.</annotation>
      </Метрики_мешающие_пользователю>
    </Уровень_Качества>
  </Пирамида_метрик>

  <Пример_продукта_ИИ_Ассистент>
      <keywords>ИИ-ассистент:9|B2B Sales:8|Solo-founder:7|unit economics:8</keywords>
      <terms>AI Assistant|B2B Sales Tool|Case Study</terms>
      <annotation>Пример применения пирамиды метрик для продукта "ИИ-ассистент для B2B продаж", разрабатываемого в режиме "соло". Демонстрирует, как основатель определяет ключевые метрики для своего бизнеса на текущем этапе.</annotation>
      
      <Пирамида_метрик_для_ИИ_Ассистента TYPE="IS_EXAMPLE_OF">
          <keywords>LTV_vs_CAC:8|Stickiness:9|Time-to-feature:8</keywords>
          <terms>LTV vs CAC|Stickiness|Time-to-feature</terms>
          <annotation>Конкретная иерархия метрик для продукта ИИ-Ассистент: Маржинальность (LTV vs CAC), Лояльность (Stickiness), Качество (Time-to-feature, как время от идеи до реализации у клиента).</annotation>
          <CrossLinks>
              <Link TARGET="Уровень_Маржинальности" TYPE="APPLIES_CONCEPT_OF" RELEVANCE="7"/>
              <Link TARGET="Sticky_Factor" TYPE="USES_METRIC" RELEVANCE="8"/>
              <Link TARGET="Уровень_Качества" TYPE="APPLIES_CONCEPT_OF" RELEVANCE="7"/>
          </CrossLinks>
      </Пирамида_метрик_для_ИИ_Ассистента>

      <NSM_для_ИИ_Ассистента_Zero_Sales_Business TYPE="IS_EXAMPLE_OF">
          <keywords>Zero Sales:9|автоматизация продаж:8|Time per Sales action:8</keywords>
          <terms>Zero Sales Business|Sales Automation</terms>
          <annotation>Пример формулировки North Star Metric (NSM) как "Zero Sales Business", где ключевая ценность — сокращение времени и затрат на продажи (Time per Sales action стремится к нулю) за счет использования ИИ.</annotation>
          <CrossLinks>
              <Link TARGET="NSM_North_Star_Metric" TYPE="IS_INSTANCE_OF" RELEVANCE="9"/>
          </CrossLinks>
      </NSM_для_ИИ_Ассистента_Zero_Sales_Business>
  </Пример_продукта_ИИ_Ассистент>

</KnowledgeGraph>