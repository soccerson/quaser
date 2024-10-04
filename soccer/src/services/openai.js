const apiKey = process.env.OPENAI_API;
import axios from 'axios';
const apiUrl = 'https://api.openai.com/v1/chat/completions';
const prompt = `
。この条件を満たしながら、２時間のサッカー練習の具体的なトレーニング内容を設計してください。また、各メニューの時間配分やセット数の提案もしてください。
ただし、必ず試合形式の練習は行ってください。
また、
練習メニュータイトル（〇〇分）
具体的な練習メニューのやり方
のように、練習内容は具体的に回答してください。`;
export async function sendMessage(message) {
  console.log(apiKey);
  try {
    const response = await axios.post(
      apiUrl,
      {
        model: 'gpt-3.5-turbo',  // 利用するモデルに応じて変更
        messages: [{ role: 'user', content: message + prompt}]
      },
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'OpenAI-Organization': 'org-BK45j1KdrprUqY0sVXjv65hn',
          'Content-Type': 'application/json'
        }
      }
    );
    console.log(response.data.choices[0].message.content)
    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('Error calling OpenAI API:', error);
    throw error;
  }
}