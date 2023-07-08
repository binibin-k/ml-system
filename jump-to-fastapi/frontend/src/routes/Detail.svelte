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

<div class="container my-3">
    <!-- 질문 -->
    <h2 class="border-bottom py-2">{question.subject}</h2>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">
                {question.content}
            </div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {question.create_date}
                </div>
            </div>
        </div>
    </div>

    <!-- 답변 목록 -->
    <h5 class="border-bottom my-3 py-2">{question.answers.length}</h5>
    {#each question.answers as answer}
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">
                {answer.content}
            </div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2">
                    {answer.create_date}
                </div>
            </div>
        </div>
    </div>
    {/each}

    <!-- 답변 등록 -->
    <Error error={error} />
    <form method="post" class="my-3">
        <div class="mb-3">
            <textarea rows="10" bind:value={content} class="form-control" />
        </div>
        <input type="submit" value="답변등록" class="btn btn-primary" on:click="{post_answer}" />
    </form>
</div>