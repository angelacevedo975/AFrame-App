slash = window.location.href.split("/")
user_id = slash[slash.length - 1]

function redirectProfile(){
    window.location.href= "http://localhost:5000/home/profile/"+user_id
}


const postForm= document.getElementById("newPost")

postForm.addEventListener("submit", e => {
    e.preventDefault()
    const data= new FormData( postForm )
    console.log( data.get("post") );
} )


const updatePosts = (posts) => {
    const container = document.getElementById("container")

    for (var i = posts.length-1; i>=0; i--) {
        const post = document.createElement("div")
        post.innerHTML = `
            <div class="card text-center mt-4">
                <div class="card-body">
                    <div class="row ml-auto" >
                        <div class="col-6">
                            <strong>  ${ posts[i].user} </strong>
                        </div>
                        <div class="col-6">
                            <strong> ${ posts[i].date} </strong> 
                        </div>
                    </div>
                    <div class="row" >
                        <div class="col-12">
                            <p> ${ posts[i].post} </p>
                        </div>
                    </div>
                </div>
            </div>
        `
        container.appendChild(post)
    }
}

const getPosts = async (user_id) => {
    const res = await fetch("http://localhost:5000/home/get", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            "_id": user_id
        })
    })

    const posts = await res.json()
    if (posts.status == 200) {
        updatePosts(posts.posts)
    }

}


getPosts(user_id)