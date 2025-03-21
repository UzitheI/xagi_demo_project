"use client";
import Image from "next/image"
import Link from "next/link"
import { ChevronDown, Eye, Heart } from 'lucide-react'
import axios from 'axios'

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { useState, useEffect } from "react"

// Define interface types
interface HumanModel {
  id: number
  name: string
  image_url: string
}

interface OutputImage {
  id: number
  human_model_id: number
  garment_id: number
  output_image_url: string
}

interface ProcessedImage {
  url: string
  name: string
  price: number
  originalPrice: number
  discount: number
}

export default function ProductPage() {
  // State to store models and images with proper typing
  const [models, setModels] = useState<HumanModel[]>([])
  const [selectedModel, setSelectedModel] = useState<number | null>(null)
  const [images, setImages] = useState<ProcessedImage[]>([])

  // Fetch human models for the dropdown
  useEffect(() => {
    async function fetchModels() {
        try {
            const response = await axios.get<HumanModel[]>('/models/human_models/');
            setModels(response.data);
          } catch (error) {
            if (axios.isAxiosError(error)) {
              console.error('Axios error: ', error.response?.data);
            } else {
              console.error('General error: ', error);
            }
          }
          
    }
    fetchModels()
  }, [])

  // Fetch output images for the selected model
  useEffect(() => {
    if (!selectedModel) return

    async function fetchImages() {
      try {
        // Using the correct endpoint for getting output images by human model
        const response = await axios.get<OutputImage[]>(`/models/output_images/human/${selectedModel}`)
        
        // Transform the response data to match expected format
        const processedImages = response.data.map((image: OutputImage): ProcessedImage => ({
          url: image.output_image_url,
          name: `Garment ${image.garment_id}`, // Hardcoded name based on garment_id
          price: 999, // Hardcoded price
          originalPrice: 1499, // Hardcoded original price
          discount: 33, // Hardcoded discount
        }))
        
        setImages(processedImages)
      } catch (error) {
        console.error("Error fetching images:", error)
      }
    }
    fetchImages()
  }, [selectedModel])

  return (
    <div className="container mx-auto px-4 py-6">
      <div className="flex flex-col space-y-4">
        {/* Header with dropdown */}
        <div className="flex justify-between items-center">
          <div className="flex items-center gap-2">
            <DropdownMenu>
              <DropdownMenuTrigger className="flex items-center gap-1 text-lg font-medium">
                {selectedModel ? models.find(m => m.id === selectedModel)?.name || "Select Model" : "Select Model"} <ChevronDown className="h-4 w-4" />
              </DropdownMenuTrigger>
              <DropdownMenuContent>
                {models.map((model) => (
                  <DropdownMenuItem
                    key={model.id}
                    onClick={() => setSelectedModel(model.id)}
                    className="font-medium"
                  >
                    {model.name}
                  </DropdownMenuItem>
                ))}
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>

        {/* Title and item count */}
        <div>
          <h1 className="text-xl font-bold">
            {selectedModel ? `${models.find(m => m.id === selectedModel)?.name || "Model"} | MEN` : "Select a Model"}
          </h1>
          <p className="text-sm text-muted-foreground">{images.length} items</p>
        </div>

        {/* Product Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
          {images.map((image, index) => (
            <div key={index} className="border rounded-lg overflow-hidden group">
              <div className="relative">
                <Image
                  src={image.url}
                  alt={image.name}
                  width={300}
                  height={400}
                  className="w-full h-[350px] object-cover"
                />
                <Button
                  variant="default"
                  className="absolute bottom-3 left-3 bg-black text-white hover:bg-black/90"
                >
                  Try & Buy
                </Button>
                <Button
                  variant="outline"
                  size="icon"
                  className="absolute top-3 right-3 bg-white/80 opacity-0 group-hover:opacity-100 transition-opacity"
                >
                  <Eye className="h-4 w-4" />
                </Button>
              </div>
              <div className="p-3">
                <div className="flex justify-between">
                  <span className="text-sm text-muted-foreground">The Souled Store</span>
                  <Button variant="ghost" size="icon" className="h-6 w-6">
                    <Heart className="h-4 w-4" />
                  </Button>
                </div>
                <h3 className="font-medium text-sm mt-1">{image.name}</h3>
                <div className="flex items-center gap-2 mt-2">
                  <span className="font-bold">₹{image.price}</span>
                  {image.discount && (
                    <span className="text-muted-foreground line-through text-sm">₹{image.originalPrice}</span>
                  )}
                  {image.discount && (
                    <span className="text-orange-500 font-medium text-sm">{image.discount}% OFF</span>
                  )}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}