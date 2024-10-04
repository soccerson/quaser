const apiKey = process.env.OPENAI_API;
import axios from 'axios';
const apiUrl = 'https://api.openai.com/v1/chat/completions';
export async function sendMessage(message) {
  try {
    const response = await axios.post(
      apiUrl,
      {
        model: 'gpt-3.5-turbo',  // 利用するモデルに応じて変更
        messages: [{ role: 'user', content: message }]
      },
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'OpenAI-Organization': 'org-BK45j1KdrprUqY0sVXjv65hn',
          'Content-Type': 'application/json'
        }
      }
    );
    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('Error calling OpenAI API:', error);
    throw error;
  }
