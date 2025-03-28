import { NextResponse } from "next/server"
import { mockModels } from "../../mock-data"

export async function GET() {
  // Simulate network delay
  await new Promise((resolve) => setTimeout(resolve, 500))

  return NextResponse.json(mockModels)
}

