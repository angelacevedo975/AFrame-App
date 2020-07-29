formulario= document.getElementById("loginForm");

const handleSubmit= async (username, password) =>{
    const res= await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify({
            username,
            password
        })
    })

    const data= await res.json()
    if(data.status == 200){
        if(data.correct){
            console.log(data.id);
            location.href= "http://localhost:5000/home/"+data.id
        }else{
            if(data.error == 1){
                document.getElementById("emailHelp").innerText= "Not user found"
            }
            if(data.error == 2){
                document.getElementById("emailHelp").innerText= "Incorrect Password"
            }
        }
    }
}

formulario.addEventListener("submit", e => {
    e.preventDefault()
    
    const form= new FormData( formulario )
    formulario.reset()
    document.getElementsByName("username")[0].focus()

    handleSubmit( form.get("username"), form.get("password") )

})


