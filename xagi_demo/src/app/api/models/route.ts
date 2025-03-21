import { NextResponse } from "next/server"

// Mock data for fallback
const mockModels = [
  { id: "model1", name: "Model A" },
  { id: "model2", name: "Model B" },
  { id: "model3", name: "Model C" },
  { id: "model4", name: "Model D" },
]

export async function GET() {
  try {
    // Try to fetch models from FastAPI backend
    try {
      const response = await fetch("http://your-fastapi-backend/models", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        // Set a shorter timeout to fail faster if the API is not available
        signal: AbortSignal.timeout(3000),
      })

      if (!response.ok) {
        throw new Error("Backend API returned an error")
      }

      const models = await response.json()
      return NextResponse.json(models)
    } catch (apiError) {
      console.warn("Could not fetch from backend API, using mock data instead:", apiError)

      // Fallback to mock data
      // Add a small delay to simulate network request
      await new Promise((resolve) => setTimeout(resolve, 300))

      return NextResponse.json(mockModels)
    }
  } catch (error) {
    console.error("Error in models API route:", error)
    return NextResponse.json({ error: "Failed to fetch models" }, { status: 500 })
  }
}

