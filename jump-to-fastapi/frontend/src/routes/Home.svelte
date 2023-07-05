<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'
    let question_list = []

    function get_question_list() {
        // fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
        //     response.json().then((json) => {
        //         question_list = json
        //     })
        // })
        fastapi('get', '/api/question/list', {}, (json) => {
            question_list = json
        })
    }
    get_question_list()
</script>

<ul>
    {#each question_list as question}
        <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
    {/each}
</ul>