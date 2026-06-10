# ufc-intelligence-dashboard
app/
├── main.py
├── config.py
├── database.py
├── models/
│   ├── fighter.py
│   ├── fight.py
│   ├── fighter_stats.py
│   └── historical_fight.py
├── schemas/
│   ├── fighter.py
│   ├── fight.py
│   └── matchup.py
├── api/v1/
│   ├── fighters.py
│   ├── fights.py
│   ├── matchups.py
│   └── odds.py
├── services/
│   ├── fighter_service.py
│   ├── matchup_service.py
│   ├── data_scraper.py
│   └── prediction_service.py
└── scrapers/
    ├── espn_scraper.py
    ├── sherdog_scraper.py
    └── ufc_scraper.py
