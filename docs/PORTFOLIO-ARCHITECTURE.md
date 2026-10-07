# Portfolio Architecture

The public portfolio is intentionally split into capability layers.

```
                     AASISH FX
                         |
        +----------------+----------------+
        |                |                |
      AI/ML          SOFTWARE/API       DATA
        |                |                |
   automation         services           ETL
   agents             integrations       SQL
   evaluation         web systems        analytics
        +----------------+----------------+
                         |
                      CLOUD
                         |
               AWS / serverless
                         |
                    OPERATIONS
                         |
               business automation
```

The projects are selected to create cross-domain evidence rather than a collection of unrelated tutorials.
