<script>
    export let error // 전달받은 오류
</script>

{#if typeof error.detail === 'string'} <!-- 일반 오류 -->
    <ul>
        <li>{error.detail}</li> <!-- 오류의 내용만 표시 -->
    </ul>
{:else if typeof error.detail === 'object' && error.detail.length > 0} <!-- 필드 오류 -->
    <ul>
        {#each error.detail as err, i} <!-- 오류를 순회하면서 필드명과 필드 오류 출력 -->
        <li>
            <strong>{err.loc[1]}</strong> : {err.msg}
        </li>
        {/each}
    </ul>
{/if}