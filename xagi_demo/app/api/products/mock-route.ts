import { NextResponse } from "next/server"
import { mockProducts } from "../../mock-data"

export async function GET(request: Request) {
  // Simulate network delay
  await new Promise((resolve) => setTimeout(resolve, 500))

  const { searchParams } = new URL(request.url)
  const model = searchParams.get("model")

  let filteredProducts = mockProducts

  if (model) {
    filteredProducts = mockProducts.filter((product) => product.model === model)
  }

  return NextResponse.json(filteredProducts)
}

