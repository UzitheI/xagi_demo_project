import Image from "next/image"
import Link from "next/link"
import { ChevronDown, Eye, Heart } from 'lucide-react'

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"

export default function ProductPage() {
  return (
    <div className="container mx-auto px-4 py-6">
      <div className="flex flex-col space-y-4">
        {/* Header with dropdown */}
        <div className="flex justify-between items-center">
          <div className="flex items-center gap-2">
            <DropdownMenu>
              <DropdownMenuTrigger className="flex items-center gap-1 text-lg font-medium">
                Garments <ChevronDown className="h-4 w-4" />
              </DropdownMenuTrigger>
              <DropdownMenuContent>
                <DropdownMenuItem className="font-medium">T-Shirts</DropdownMenuItem>
                <DropdownMenuItem>Shirts</DropdownMenuItem>
                <DropdownMenuItem>Jeans</DropdownMenuItem>
                <DropdownMenuItem>Trousers</DropdownMenuItem>
                <DropdownMenuItem>Jackets</DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>

        {/* Title and item count */}
        <div>
          <h1 className="text-xl font-bold">T-Shirts | MEN</h1>
          <p className="text-sm text-muted-foreground">539 items</p>
        </div>

        {/* Filter and Sort */}
        <div className="flex justify-between items-center">
          <div className="flex gap-2">
            <Badge variant="outline" className="flex items-center gap-1 px-3 py-1.5 rounded-md bg-background">
              T-Shirts
              <button className="ml-1 text-muted-foreground">×</button>
            </Badge>
          </div>
          <div className="relative w-48">
            <DropdownMenu>
              <DropdownMenuTrigger className="w-full flex items-center justify-between border p-2 rounded-md">
                <span>Sort By</span>
                <ChevronDown className="h-4 w-4" />
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end" className="w-48">
                <DropdownMenuItem>What's new</DropdownMenuItem>
                <DropdownMenuItem>Price-high to low</DropdownMenuItem>
                <DropdownMenuItem>Price-low to high</DropdownMenuItem>
                <DropdownMenuItem>Discount</DropdownMenuItem>
                <DropdownMenuItem>Customer Rating</DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>

        {/* Product Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mt-4">
          {/* Product 1 */}
          <div className="border rounded-lg overflow-hidden group">
            <div className="relative">
              <Image 
                src="/placeholder.svg?height=400&width=300" 
                alt="Solid Plum T-Shirt" 
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
              <h3 className="font-medium text-sm mt-1">Solids: Plum</h3>
              <div className="flex items-center gap-2 mt-2">
                <span className="font-bold">₹649</span>
                <span className="text-muted-foreground line-through text-sm">₹999</span>
                <span className="text-orange-500 font-medium text-sm">35% OFF</span>
              </div>
            </div>
          </div>

          {/* Product 2 */}
          <div className="border rounded-lg overflow-hidden group">
            <div className="relative">
              <Image 
                src="/placeholder.svg?height=400&width=300" 
                alt="Doberman Men Printed T-Shirt" 
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
              <div className="absolute bottom-3 right-3 bg-black/70 text-white text-xs px-2 py-1 rounded">
                OVERSIZED FIT
              </div>
            </div>
            <div className="p-3">
              <div className="flex justify-between">
                <span className="text-sm text-muted-foreground">Pronk</span>
                <Button variant="ghost" size="icon" className="h-6 w-6">
                  <Heart className="h-4 w-4" />
                </Button>
              </div>
              <h3 className="font-medium text-sm mt-1">Doberman Men Printed Premium Oversized Terry T-Shirt</h3>
              <div className="flex items-center gap-2 mt-2">
                <span className="font-bold">₹799</span>
                <span className="text-muted-foreground line-through text-sm">₹1599</span>
                <span className="text-orange-500 font-medium text-sm">50% OFF</span>
              </div>
            </div>
          </div>

          {/* Product 3 */}
          <div className="border rounded-lg overflow-hidden group">
            <div className="relative">
              <Image 
                src="/placeholder.svg?height=400&width=300" 
                alt="Wrath Wings Men Printed T-Shirt" 
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
              <div className="absolute bottom-3 right-3 bg-black/70 text-white text-xs px-2 py-1 rounded">
                OVERSIZED FIT
              </div>
            </div>
            <div className="p-3">
              <div className="flex justify-between">
                <span className="text-sm text-muted-foreground">Pronk</span>
                <Button variant="ghost" size="icon" className="h-6 w-6">
                  <Heart className="h-4 w-4" />
                </Button>
              </div>
              <h3 className="font-medium text-sm mt-1">Wrath Wings Men Printed Premium Oversized Terry T-Shirt</h3>
              <div className="flex items-center gap-2 mt-2">
                <span className="font-bold">₹799</span>
                <span className="text-muted-foreground line-through text-sm">₹1599</span>
                <span className="text-orange-500 font-medium text-sm">50% OFF</span>
              </div>
            </div>
          </div>

          {/* Product 4 */}
          <div className="border rounded-lg overflow-hidden group">
            <div className="relative">
              <Image 
                src="/placeholder.svg?height=400&width=300" 
                alt="Bewakoof Men's Black Valhalla Typography T-Shirt" 
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
                <span className="text-sm text-muted-foreground">Bewakoof</span>
                <Button variant="ghost" size="icon" className="h-6 w-6">
                  <Heart className="h-4 w-4" />
                </Button>
              </div>
              <h3 className="font-medium text-sm mt-1">Bewakoof Men's Black Valhalla Typography T-Shirt</h3>
              <div className="flex items-center gap-2 mt-2">
                <span className="font-bold">₹449</span>
                <span className="text-muted-foreground line-through text-sm">₹999</span>
                <span className="text-orange-500 font-medium text-sm">55% OFF</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
