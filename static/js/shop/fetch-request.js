function sendRequest(method, url, body= null, headers = null) {
   // const headers = {
   //     'Content-Type': 'application/json'
   // }
    return fetch(url, {
       method: method,
       body: JSON.stringify(body),
       headers: headers
   }).then(response => {
       if (response.ok){
           return response.json()
       }
       return response.json().then(error => {
           const e = new Error('Something goes wrong')
       })

   }
)

}
