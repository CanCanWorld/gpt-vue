import Antd from 'ant-design-vue';
import { createApp } from 'vue'
import App from '@/App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)
app.mount('#app')
app.use(Antd)
app.use(ElementPlus)
