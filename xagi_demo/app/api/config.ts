export const API_CONFIG = {
  // Set this to your actual FastAPI backend URL when available
  baseUrl: process.env.NEXT_PUBLIC_API_URL || null,

  // Whether to use mock data (true) or try to connect to the real API (false)
  useMockData: process.env.NEXT_PUBLIC_USE_MOCK_DATA === "true" || true,

  // Timeout for API requests in milliseconds
  timeout: 5000,
}

