<template>
  <!-- demo/textInput are examples of passing an object directly into a property (if this does not work refer to data values like in the initialMessages example) -->
  <!-- initialMessages is an example of passing a data object into a property -->
  <div id="app">
    <div class="main-container">
      <div class="left-container">
        <div style = "margin-top:20px;">
        <h2>AGInsider</h2>
        </div>
        <div class="chat">
          <deep-chat 
            class="wide-chat"
            :initialMessages="initialMessages"
            :request="chatRequest"
            :messageStyles="messageStyles"
            :submitButtonStyles="submitButtonStyles"
            :textInput="textInputStyles"
            :auxiliaryStyle="auxiliaryStyle"
            :avatars="avatarsObject"
            gifs='{"button": {"position": "dropup-menu"}}'
            audio='{"button": {"position": "dropup-menu"}}'
            camera='{"button": {"position": "dropup-menu"}}'
            mixedFiles='{"button": {"position": "inside-left"}}'
            textToSpeech='{"volume": "0.9"}'
            introMessage='{"text": "Send a message to hear the response."}'
            style="border-radius: 8px"
            demo="true"
            speechToText='{
              "webSpeech": true,
              "translations": {"hello": "goodbye", "Hello": "Goodbye"},
              "commands": {"resume": "resume", "settings": {"commandMode": "hello"}},
              "button": {"position": "outside-left"}
            }'
          ></deep-chat>
        </div>
      </div>
      <div class="sidebar" @click="sidebarClick">
        <div class ="top-bar" />
        <img src="..\assets\mascot-20231126110627.gif"/>
      </div>
    </div>
  </div>

</template>

<script>
import "deep-chat";
import axios from 'axios';
import imgMeUrl from '../assets/me.png';
import imgAIUrl from '../assets/AI.png';

export default {
  data() {
    return {
      avatarsObject: {
        ai: {
          src: imgAIUrl
        },
        user:{
          src: imgMeUrl
        }
      },
      introMessage: { text: "您好！我将会问您三个问题，请依次回答它们。" },
      initialMessages: [
        { text: "您好！请问您的职业是什么，可以简单地介绍一下自己吗？", role: "ai" },
      ],
      questions: [
        "请告诉我您对人工通用智能（AGI）的了解程度，是否有相关学术或实践经验？",
        "在AI的世界中，哪些特定的领域或话题让您特别感兴趣？或者有没有什么特别的人物、事件或术语让您好奇，您希望深入了解？",
      ],
      currentQuestionIndex: 0,
      userAnswers: [],
      aiAnswers: [],
      messageStyles: {
        default: {
          user: {
            bubble: { backgroundColor: "#2670ff" }
          },
          ai: {
            bubble: { backgroundColor: "#004f97", color: "white" }
          }
        }
      },
      submitButtonStyles: {
        submit: {
          svg: {
            styles: {
              default: {
                filter: "brightness(0) saturate(100%) invert(60%) sepia(79%) saturate(643%) hue-rotate(185deg) brightness(102%) contrast(100%)"
              }
            }
          }
        }
      },
      textInputStyles: {
        styles: {
          container: {
            backgroundColor: "#004f97",
            color: "white",
            boxShadow: "unset"
          }
        },
        placeholder: { style: { color: "#d1d1d1" } }
      },
      auxiliaryStyle: `
        ::-webkit-scrollbar-thumb {
          background-color: #0174db;
        }
        ::-webkit-scrollbar-track {
          background-color: unset;
        }
      `
    };
  },
  computed: {
    chatRequest() {
      return {
        handler: this.handleMessage
      };
    }
  },
  methods: {
    sidebarClick(){
      alert("开始场景练习，开会震惊众人 AGI ！")
    },
    async handleMessage(body, signals) {
      if (this.currentQuestionIndex === 0) {
      // 第一个问题的答案前加上 '职业和介绍'
        this.userAnswers.push('职业和介绍: ' + body.messages[0].text);
        console.log('第一个',this.currentQuestionIndex, this.userAnswers);
      } else if (this.currentQuestionIndex === 1) {
        // 第二个问题的答案前加上 'AGI了解程度'
        this.userAnswers.push('AGI了解程度: ' + body.messages[0].text);
        console.log('第二个',this.currentQuestionIndex, this.userAnswers);
      } else if (this.currentQuestionIndex === 2) {
        // 第三个问题的答案前加上 '感兴趣的特定领域和话题'
        this.userAnswers.push('感兴趣的特定领域和话题: ' + body.messages[0].text);
        console.log('第三个',this.currentQuestionIndex, this.userAnswers)
      }
      console.log(body.messages[0].text)
      console.log(this.userAnswers)
      console.log(this.currentQuestionIndex);
      if (this.currentQuestionIndex < this.questions.length) {
        // 提出下一个问题
        signals.onResponse({ text: this.questions[this.currentQuestionIndex], role: "ai" });
        this.currentQuestionIndex++;
      } else if(this.currentQuestionIndex == this.questions.length){
        // 所有问题都已回答，发送答案到后端
        const data = await this.sendAnswersToBackend();
        console.log(data)
        console.log('data.response', data.response)
        const aiAnswers1 =  '<div class="feedback"> '+
          '<span class="feedback-text"> \n延申阅读: \n</span> '+
          '<img class="feedback-icon feedback-icon-positive"onclick = "alert(\'追寻这个单词的历史来源,理解来源 AGI ！\')" style="height: 20px;" src="/lsqy.png"> '+
          '<img class="feedback-icon feedback-icon-positive"onclick = "alert(\'sam 正在牛津大学的演讲里使用这个单词，引爆点，追随Sam 脚步\')" style="height: 20px;" src="/dqrd.png"> '+
          '<img class="feedback-icon feedback-icon-negative"onclick = "alert(\'开始场景练习，语音对话，彻底掌握 AGI，开会震惊众人 AGI ！\')" style="height: 20px;" src="/cjxx.png"> </div>'
      
          signals.onResponse({ text: data.response, role: "ai" ,html: aiAnswers1 });
          this.userAnswers.push('AGI了解程度: ' + body.messages[0].text);
      }
    },
    async sendAnswersToBackend() {
      const combinedAnswers = this.userAnswers.join(','); // 将答案数组转换为一个字符串
      console.log('combined', combinedAnswers)
      try {
        const response = await axios.post('http://127.0.0.1:8000/process_input/', combinedAnswers, {
          headers: {
            'Content-Type': 'text/plain'
          }
        });
        const data = response.data;
        // 处理或显示后端响应
        console.log(data);
        return data;  // 返回后端响应
      } catch (error) {
        console.error('API 请求错误:', error);
      }
    }
  }
};
</script>

<style>

 /* 全局样式 */
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  /* 应用的基础样式 */
  #app {
    font-family: sans-serif;
    display: flex;
    flex-direction: column;
    height: 100vh;
  }

  /* 头部标题样式 */
  h2 {
    text-align: center;
    padding: 20px 0;
  }

  /* 主容器样式 */
  .main-container {
    display: flex;
    flex: 1;
  }

  /* 聊天容器样式 */
  .left-container {
    display:flex;
    flex: 1;
    flex-direction: column; /* 子元素垂直排列 */
    align-items: center; /* 水平居中 */
    /* 如果需要滚动，可以取消注释以下样式 */
    /* overflow-y: auto; */
  }
  
  .chat{
    margin-top: 20px;
    justify-content: center; /* 垂直居中 */
    align-items: center; /* 水平居中 */
  }

  /* 聊天框样式 */
  .wide-chat {
    /* 根据需要调整宽度 */
    width: 1200px !important; 
    height: 1000px !important;
  }

  /* 侧边栏样式 */
  .sidebar {
    width: 400px; /* 侧边栏宽度，您可以根据需要进行调整 */
  }

  /* 侧边栏图片样式 */
  .sidebar img {
    margin-top:100px;
    margin-right:100px;
    width: 100%;
    height: auto;
    /* 如果需要边框圆角，可以取消注释以下样式 */
    /* border-radius: 5px; */
  }
  .feedback-icon {
    height: 20px;
  }
</style>

