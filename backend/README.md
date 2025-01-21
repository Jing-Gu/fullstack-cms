### Local dev
```
fastapi dev
```

### Endpoints
/portfolios

/news

/supports

```
http://127.0.0.1:8000/api/v1/portfolios/list
```

### ADR

http://127.0.0.1:8000/api/v1/news

[ ] The user can create a new news item. - POST

[ ] The user can view all the news. - GET


http://127.0.0.1:8000/api/v1/portfolios/{revenue-fixe}/reports

[ x ] The user can create new report.  - POST

[ x ] The user can view all the reports. - GET


http://127.0.0.1:8000/api/v1/portfolios/{revenue-fixe}/reports/{uuid}

[ x ] The user can read the existing report. - GET

[   ] The user can modify the existing report. - PUT / PATCH ?

[   ] The user can delete the existing report. - DELETE


http://127.0.0.1:8000/api/v1/portfolios/{revenue-fixe}/menu

[   ] The user can define the menu (add, modify ) - POST

[ x ] The app can receive the portfolio menu as json object - GET


#### DB choices - DynamoDB vs PostgreSQL
Data Model

- DynamoDB: A NoSQL database that supports key-value and document data models, schemaless, allowing for flexible data structures.
- PostgreSQL: A relational database that uses a well-defined schema. It supports complex queries, foreign keys, triggers, and updatable views.

Performance and Scalability
- DynamoDB: Designed for high performance with single-digit millisecond latency. It can handle more than 10 trillion requests per day and supports automatic scaling.
- PostgreSQL: Performance depends on the disk subsystem and database design. It supports advanced indexing, partitioning, and just-in-time (JIT) compilation to optimize performance.

Use Cases
- DynamoDB: Ideal for applications requiring high throughput and low latency, such as real-time bidding platforms, gaming leaderboards, and IoT data management.
- PostgreSQL: Suitable for applications needing complex data modeling and transactions, such as enterprise applications, geospatial data management, and business intelligence.

Ease of Management
- DynamoDB: Fully managed by AWS, requiring no server management or maintenance
- PostgreSQL: Requires more hands-on management unless using a managed service like AWS RDS.

> [!NOTE]
> Final choice: DynamoDB

> Reason:
- DynamoDB is a NoSQL database, which means it is highly flexible and can handle nested data structures. Each item in a DynamoDB table can have a different set of attributes, which allows for a lot of flexibility.

- DynamoDB supports CRUD operations through its API
  - Create: Use the `PutItem` operation to add new items to your tables.
  - Read: Use the `GetItem` operation to retrieve items by their primary key.
  - Update: Use the `UpdateItem` operation to modify existing items.
  - Delete: Use the `DeleteItem` operation to remove items from your tables.