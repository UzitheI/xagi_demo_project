import { NextResponse } from "next/server"

// Mock data for fallback
const mockProducts = [
  {
    id: 1,
    name: "Solids: Plum",
    brand: "The Souled Store",
    price: 649,
    originalPrice: 999,
    discount: 35,
    image: "/placeholder.svg?height=400&width=300",
    model: "model1",
  },
  {
    id: 2,
    name: "Doberman Men Printed Premium Oversized Terry T-Shirt",
    brand: "Pronk",
    price: 799,
    originalPrice: 1599,
    discount: 50,
    image: "/placeholder.svg?height=400&width=300",
    model: "model2",
  },
  {
    id: 3,
    name: "Wrath Wings Men Printed Premium Oversized Terry T-Shirt",
    brand: "Pronk",
    price: 799,
    originalPrice: 1599,
    discount: 50,
    image: "/placeholder.svg?height=400&width=300",
    model: "model3",
  },
  {
    id: 4,
    name: "Bewakoof Men's Black Valhalla Typography T-Shirt",
    brand: "Bewakoof",
    price: 449,
    originalPrice: 999,
    discount: 55,
    image: "/placeholder.svg?height=400&width=300",
    model: "model4",
  },
]

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url)
    const model = searchParams.get("model")

    // Try to fetch from FastAPI backend
    try {
      // Build the API URL based on whether a model filter is applied
      let apiUrl = "http://your-fastapi-backend/products"
      if (model) {
        apiUrl += `?model=${model}`
      }

      const response = await fetch(apiUrl, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        // Set a shorter timeout to fail faster if the API is not available
        signal: AbortSignal.timeout(3000),
      })

      if (!response.ok) {
        throw new Error("Backend API returned an error")
      }

      const products = await response.json()
      return NextResponse.json(products)
    } catch (apiError) {
      console.warn("Could not fetch from backend API, using mock data instead:", apiError)

      // Fallback to mock data
      let filteredProducts = mockProducts
      if (model) {
        filteredProducts = mockProducts.filter((product) => product.model === model)
      }

      // Add a small delay to simulate network request
      await new Promise((resolve) => setTimeout(resolve, 300))

      return NextResponse.json(filteredProducts)
    }
  } catch (error) {
    console.error("Error in products API route:", error)
    return NextResponse.json({ error: "Failed to fetch products" }, { status: 500 })
  }
}

