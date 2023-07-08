<script>
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"

    export let params = {} // Detail 컴포넌트 호출 시 전달한 파라미터를 담을 변수
    let question_id = params.question_id
    let question = {answers:[]} // 비동기로 진행되므로 먼저 조회될 때 오류 발생을 방지
    let content = ""
    let error = {detail:[]}

    function get_question() {
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
            question = json
        })
    }

    get_question()

    function post_answer(event) {
        event.preventDefault() // submit 버튼이 눌릴 경우 form이 자동으로 전송되는 것을 방지
        let url = "/api/answer/create/" + question_id
        let params = {
            content: content
        }
        fastapi('post', url, params,
            (json) => { // success_callback
                content = '' // 이전의 content를 초기화
                error = {detail:[]} // 이전의 error 변수를 초기화
                get_question() // 등록된 답변이 반영되도록 질문 상세화면을 다시 불러옴
            },
            (err_json) => { // failure_callback
                error = err_json
            }
        )
    }
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>
<ul>
    {#each question.answers as answer}
        <li>{answer.content}</li>
    {/each}
</ul>
<Error error={error} /> <!-- Error 컴포넌트 추가 -->
<form method="post">
    <textarea rows="15" bind:value={content}></textarea>
    <input type="submit" value="답변등록" on:click="{post_answer}">
</form>