<template>
  <h1>AGInsider</h1>
  <!-- demo/textInput are examples of passing an object directly into a property (if this does not work refer to data values like in the initialMessages example) -->
  <!-- initialMessages is an example of passing a data object into a property -->
  <div class="chat-container">
    <deep-chat 
      class="wide-chat"
      :initialMessages="initialMessages"
      :request="chatRequest"
      :messageStyles="messageStyles"
      :submitButtonStyles="submitButtonStyles"
      :textInput="textInputStyles"
      :auxiliaryStyle="auxiliaryStyle"
    ></deep-chat>
  </div>
</template>

<script>
import "deep-chat";
import axios from 'axios';

export default {
  data() {
    return {
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
      } // 收集用户答案
      // console.log(body.messages[0].text);
      // console.log(this.userAnswers);
      // console.log(this.currentQuestionIndex);
      if (this.currentQuestionIndex < this.questions.length) {
        // 提出下一个问题
        signals.onResponse({ text: this.questions[this.currentQuestionIndex], role: "ai" });
        this.currentQuestionIndex++;
      } else if (this.currentQuestionIndex == this.questions.length){
        // 所有问题都已回答，发送答案到后端
        const data = await this.sendAnswersToBackend();
        console.log(data)
        console.log('data.response', data.response)
        signals.onResponse({ text: data.response, role: "ai"  });
      }
    },
    async sendAnswersToBackend() {
      const combinedAnswers = this.userAnswers.join(','); // 将答案数组转换为一个字符串
      console.log('combined', combinedAnswers)
      try {
        const response = await axios.post('http://127.0.0.1:8000/get_demand/', combinedAnswers, {
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
div {
  font-family: sans-serif;
  text-align: center;
  justify-content: center;
  display: grid;
  width: 100%;
}
.chat-container {
  font-family: sans-serif;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.wide-chat {
  border-radius: 10px;
  width: 98vw; /* 调整为所需的宽度 */
  height: calc(100vh - 70px);
  padding-top: 10px;
  /* 可以添加其他样式 */
}
</style>

