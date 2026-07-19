import axios from "axios";

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "/api/v1",
  headers: {
    "Content-Type": "application/json",
    "X-Demo-Token": "token_operator", // default demo token
  },
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    // Centralized error handling
    if (error.response?.status === 503) {
      console.error("AI service is currently unavailable");
    }
    return Promise.reject(error);
  }
);
