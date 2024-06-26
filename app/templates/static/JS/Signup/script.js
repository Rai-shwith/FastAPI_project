document.getElementById('signupForm').addEventListener('submit', function (event) {
    event.preventDefault()
    const name = document.getElementById('signupName').value;
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;
    const credentials = {
        "user_name": name,
        "email": email,
        "password": password
    };
    fetch('/users/api/token', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    }).then(response => {
        if (!response.ok) {
            if (response.status== 422){
                console.error(response.statusText)
                const message = document.getElementById('center');
                message.style.display='block';
                document.getElementById('page-body').classList.add('body-opacity');
                setTimeout(() => {

                        message.style.display='none';
                        document.getElementById('page-body').classList.remove('body-opacity');
                        
                }, 1500);
                
            }
            else if (response.status== 409){
                console.error(response.statusText)
                const message = document.getElementById('center');
                message.innerHTML='Email Already Exist'
                message.style.display='block';
                document.getElementById('page-body').classList.add('body-opacity');
                setTimeout(() => {

                        message.style.display='none';
                        message.innerHTML='Invalid Email'
                        document.getElementById('page-body').classList.remove('body-opacity');
                        
                }, 1500);
                
            }
            throw new Error("Error while sending info: ",response.statusText)
        }
        return response.json()
    }).then(userinfo => {
        const formdata = new FormData();
        formdata.append('username', userinfo.email);
        formdata.append('password', credentials.password);
        fetch('/api/token', {
            method: 'POST',
            body: formdata
        }).then(response => {
            if (!response.ok) {
                throw new Error("Error while receiving token: ",response.statusText)
            }
            return response.json()
        }).then(data =>{
            localStorage.setItem('token', data.acess_token);
                localStorage.setItem('tokenType', data.token_type);
                const message = document.getElementById('center');
                message.innerHTML='Successfully Signed up'
                message.style.color='green'
                message.style.display='block';
                document.getElementById('page-body').classList.add('body-opacity');
                setTimeout(() => {
                    window.location.href = "/posts"
                    setTimeout(() => {
                            document.getElementById('signupName').value=''
                            document.getElementById('signupEmail').value=''
                            document.getElementById('signupPassword').value=''          
                            message.style.display='none';
                        message.innerHTML='Invalid Email'
                        document.getElementById('page-body').classList.remove('body-opacity');
                        }, 1000);
                        
                        
                }, 1500);
                
        })
    })
})