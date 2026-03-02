import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { catchError, finalize, of } from 'rxjs';

import { AlbumService } from '../services/album.service';
import { Photo } from '../models/photo.model';

@Component({
  selector: 'app-album-photos',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './album-photos.html',
  styleUrl: './album-photos.css'
})
export class AlbumPhotos implements OnInit {
  albumId!: number;

  photos: Photo[] = [];
  loading = false;
  errorMsg = '';

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService
  ) {}

  ngOnInit(): void {
    this.albumId = Number(this.route.snapshot.paramMap.get('id'));
    this.loadPhotos();
  }

  loadPhotos() {
    this.loading = true;
    this.errorMsg = '';

    this.albumService.getAlbumPhotos(this.albumId)
      .pipe(
        catchError(() => {
          this.errorMsg = 'Failed to load photos.';
          return of([]);
        }),
        finalize(() => (this.loading = false))
      )
      .subscribe(data => {
        this.photos = data;
      });
  }
}
