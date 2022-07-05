# Project-F

# Project requirements
|                |                               |
|----------------|-------------------------------|
|1|`Tickets - agents can list them all or by id` |
|2|`Tickets  - agents can delete, modify and create them` |
|3|`Statuses - agents can list them all or by id` |
|4|`Statuses  - agents can delete, modify and create them` |
|5|`Levels - agents can list them all or by id` |
|6|`Levels  - agents can delete, modify and create them` |
|7|`Ticket Types - agents can list them all or by id`|
|8|`Ticket Types  - agents can delete, modify and create them`|
|9|`Agents can request for a token`|
|10|`Agents can use the token to make queries`|
|11|`Customers - agents can list them all or by id`|
|12|`Customers  - agents can delete, modify and create them`|
|13|`Sending emails while creating new agent accounts (with rabbitmq queue)`|
|14|`Agents can limit number of record in the result`|
|15|`API documentation (/docs)`|
|16|`Containerization - Docker`|


# Usage
1. Clone this repo
2. Open this project in command line
3. Rename example.dev file to dev.env
4. Type docker-compose up in the terminal
5. Open localhost:8080, login: username: root, password: root, database: master, Click SQL query button (left-hand-upper corner of the browser), copy the contents of the sqldump.sql file and paste it into the text area and hit "Perform"