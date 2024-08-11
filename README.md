   # Chat Reader: Usage Guide

   ## Overview

   Chat Reader is a web platform designed for conveniently viewing conversations between users and assistant bots, such as Telegram or WhatsApp bots. This project allows developers to review conversations to ensure the correctness of bot operations and identify potential errors in code or the database.

   ## Installation and Setup

   1. **Clone the Repository**

      First, clone the repository to your local machine:
      ```bash
      git clone <REPOSITORY_URL>
      cd chat-reader
      ```

   2. **Install Dependencies**

      Ensure you have Python and pip installed. Then, install the required dependencies:
      ```bash
      pip install -r requirements.txt
      ```

   3. **Set Up Environment**

      Create a `.env` file in the root directory of the project and add your database URL:
      ```plaintext
      DATABASE_URL=<your_database_url>
      ```

   4. **Run the Application**

      Start the server using:
      ```bash
      python app.py
      ```
      The server will be available at `http://127.0.0.1:5000` by default.

   ## Using the Platform

   1. **Access the Platform**

      Open your browser and go to `http://127.0.0.1:5000`.

   2. **Load Data**

      Click the "Load Data" button to fetch and display conversations from the database.

   3. **View Conversations**

      - **User List:** The left side of the screen shows a list of users. Click on a user’s name to view their conversations.
      - **Chat:** The right side of the screen displays messages from the selected user in chronological order.

   ## Project Structure

   - `app.py`: Main application file containing server logic.
   - `static/css/styles.css`: Styles for visual appearance.
   - `static/js/script.js`: Scripts for webpage functionality.
   - `templates/index.html`: HTML template for the main page.

   ## Notes

   - Ensure your database is set up and contains the `user_messages` and `bot_messages` tables with appropriate data.
   - In case of errors, check the server console and debug the code based on the error messages received.

