document.addEventListener('DOMContentLoaded', function () {
    const chatColumns = document.getElementById('chatColumns');
    const userList = document.getElementById('userList');
    const fetchDataBtn = document.getElementById('fetchDataBtn');
    let usersData = {}; // Stores data about users and their messages

    fetchDataBtn.addEventListener('click', fetchData);

    function fetchData() {
        chatColumns.innerHTML = ''; // Clear previous messages before loading new ones
        userList.innerHTML = ''; // Clear user list before loading new users
        usersData = {}; // Clear user data

        fetch('/messages')
            .then(response => response.json())
            .then(data => {
                data.forEach(message => {
                    const userName = message.name;
                    if (!usersData[userName]) {
                        usersData[userName] = [];
                        addUserToUserList(userName);
                    }
                    usersData[userName].push(message);
                });
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    function addUserToUserList(userName) {
        const userItem = document.createElement('div');
        userItem.textContent = userName;
        userItem.addEventListener('click', () => {
            showChatForUser(userName);
        });
        userList.appendChild(userItem);
    }

    function showChatForUser(userName) {
        chatColumns.innerHTML = ''; // Clear previous messages
        const userMessages = usersData[userName];
        userMessages.forEach(message => {
            const messageElem = createMessage(message);
            chatColumns.appendChild(messageElem);
        });
    }

    function createMessage(data) {
        const message = document.createElement('div');
        message.classList.add('message');

        const userInfo = document.createElement('div');
        userInfo.classList.add('user-info');
        userInfo.textContent = data.type === 'user' ? `${data.name}` : `BOT(${data.name})`; // Display user name or bot name
        message.appendChild(userInfo);

        const messageText = document.createElement('div');
        messageText.classList.add('message-text');
        messageText.textContent = data.message; // Display the message text
        message.appendChild(messageText);

        const timestamp = document.createElement('div');
        timestamp.classList.add('timestamp');
        timestamp.textContent = `Sent at ${data.timestamp}`; // Display the timestamp
        message.appendChild(timestamp);

        return message;
    }

    // Initial data load
    fetchData();
});
