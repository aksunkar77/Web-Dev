import { Routes } from '@angular/router';

import { Home } from './home/home';
import { About } from './about/about';
import { Albums } from './albums/albums';
import { AlbumDetail } from './album-detail/album-detail';
import { AlbumPhotos } from './album-photos/album-photos';

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },

  { path: 'home', component: Home },
  { path: 'about', component: About },

  {
    path: 'albums',
    component: Albums,
    children: [
      { path: ':id', component: AlbumDetail },
      { path: ':id/photos', component: AlbumPhotos }
    ]
  },

  { path: '**', redirectTo: 'home' }
];