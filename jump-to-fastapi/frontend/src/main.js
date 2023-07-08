import './app.css'

// node_modules 디렉터리에 있는 파일은 상대경로 사용 가능
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'

import App from './App.svelte'

const app = new App({
  target: document.getElementById('app'),
})

export default app