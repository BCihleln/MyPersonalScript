# Usage Memo

Deploy n8n via docker : `docker compose --env-file .env up` 
- Configure local parameters : `.env` file
- Retrieve previous n8n set up : `database.sqlite` file  
    Copy and paste the file into volume path  
- If you had not set the `N8N_ENCRYPTION_KEY` in `.env` file when previous n8n been deployed  
    - **remember to reset credentials**  
    - Reconfigure every nodes that use credentials