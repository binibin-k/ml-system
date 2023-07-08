const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params)

    let _url = import.meta.env.VITE_SERVER_URL + url
    if(method === 'get') {
        _url += "?" + new URLSearchParams(params) // get 방식에 맞도록 url에 파라미터를 연결
    }

    let options = {
        method: method,
        headers: {
            "Content-Type": content_type
        }
    }

    if(method !== 'get') { // get 방식이 아닌 경우 options에 body(json으로 변환한 파라미터)를 추가
        options['body'] = body
    }

    fetch(_url, options)
        .then(response => {
            if(response.status == 204) { // No Content인 경우
                if(success_callback) {
                    success_callback()
                }
                return // response.status가 204인 경우 이하 코드가 실행되지 않도록 함 (반환할 응답이 없기 때문)
            }
            response.json()
                .then(json => {
                    if(response.status >= 200 && response.status < 300) { // 요청이 성공한 경우
                        if(success_callback) {
                            success_callback(json)
                        }
                    } else { // 요청이 실패한 경우
                        if(failure_callback) { // 수행할 함수가 있는 경우
                            failure_callback(json)
                        }else { // 수행할 함수가 없는 경우
                            alert(JSON.stringify(json)) // 경고
                        }
                    }
               })
                .catch(error => { // ?
                    alert(JSON.stringify(error))
                })
            })
        }

export default fastapi