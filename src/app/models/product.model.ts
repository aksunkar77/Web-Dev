export interface Product {
  id: number;
  categoryId: number;
  name: string;
  price: number;
  oldPrice?: number;      
  rating: number;         
  reviews: number;
  imageUrl: string;
  link: string;

  monthlyPrice?: number;
  months?: number;

  
  cashbackPercent?: number; 
  timerText?: string;  
}     