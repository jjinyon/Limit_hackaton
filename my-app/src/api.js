import axios from 'axios';

const API_ENDPOINT = 'YOUR_API_ENDPOINT';
const ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN';

export const callHyperCLOVA = async (clovaRequestPayload) => {
  try {
    const response = await axios.post(API_ENDPOINT, clovaRequestPayload, {
      headers: {
        Authorization: `Bearer ${ACCESS_TOKEN}`,
        'X-NCP-CLOVASTUDIO-REQUEST-ID': Math.random().toString()
      }
    });
    return response.data;
  } catch (error) {
    console.error('Error calling HyperCLOVA API:', error);
    throw error;
  }
};