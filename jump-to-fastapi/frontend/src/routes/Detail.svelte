<script>
    import fastapi from "../lib/api"

    export let params = {} // Detail 컴포넌트 호출 시 전달한 파라미터를 담을 변수
    let question_id = params.question_id
    let question = {} // 한 건의 질문에 대한 상세정보이므로 초기화 필요

    function get_question() {
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
            question = json
        })
    }

    get_question()
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>