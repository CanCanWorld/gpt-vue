
<script setup lang="ts">

import {onMounted, ref} from "vue";
import {msgApi} from "@/common/network";
import {message} from "ant-design-vue";
import logo from '@/assets/logo.jpg'

const msg = ref('')
const chats = ref<{ msg: string, isQ: boolean }[]>([])

const onAskClick = () => {
    if (msg.value == '') {
        message.warning('请输入问题！');
        return
    }
    chats.value.push({
        msg: msg.value,
        isQ: true
    })
    getMsg()
}

const getMsg = async () => {
    const res = await msgApi(msg.value)
    console.log(res.data)
    chats.value.push({
        msg: res.data,
        isQ: false
    })
}

onMounted(() => {
})
</script>
<template>
    <div class="chats">
        <div class="chat" v-for="(item, index) in chats" :key="index">
            <div class="question" v-if="item.isQ">
                {{ item.msg }}
            </div>
            <div class="answer" v-else>
                <div class="header">
                    <img class="face" :src="logo" alt=""/>
                    猫娘小糖
                </div>
                {{ item.msg }}
            </div>
        </div>
    </div>
    <el-affix position="bottom" :offset="0">
        <div class="message-box">
            <el-input
                v-model="msg"
                :autosize="{ minRows: 2, maxRows: 4 }"
                type="textarea"
                placeholder="请输入提问信息"
            />
            <el-button type="primary" round class="button" @click="onAskClick">提问</el-button>
        </div>
    </el-affix>
    <!--    <a-affix offset-bottom="0">-->
    <!--        <a-flex class="message-box" :vertical="false">-->
    <!--            <a-textarea-->
    <!--                    class="input"-->
    <!--                    allow-clear-->
    <!--                    v-model:value="msg"-->
    <!--                    placeholder="请输入提问信息"/>-->
    <!--            <a-button class="button" @click="onAskClick">提问</a-button>-->
    <!--        </a-flex>-->
    <!--    </a-affix>-->
</template>

<style scoped>

.chats {
    padding-bottom: 100px;

    .chat {
        padding: 10px;

        .question {
            padding: 20px;
            border-radius: 30px;
            border: #e7edf1 solid 2px;
        }

        .answer {
            padding: 20px;
            border-radius: 30px;
            background-color: #e7edf1;

            .header {
                display: flex;
                flex-direction: row;
                align-items: center;
                gap: 10px;
                margin-bottom: 10px;
                color: #505050;

                .face {
                    border-radius: 40px;
                    width: 50px;
                    height: 50px;
                }
            }
        }
    }
}

.message-box {
    width: 100%;
    position: absolute;
    bottom: 0;
    padding: 20px;
    gap: 10px;
}
</style>
