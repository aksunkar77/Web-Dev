import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { catchError, finalize, of } from 'rxjs';

import { AlbumService } from '../services/album.service';
import { Album } from '../models/album.model';

@Component({
  selector: 'app-albums',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './albums.html',
  styleUrl: './albums.css'
})
export class Albums implements OnInit {
  albums: Album[] = [];
  loading = false;
  errorMsg = '';

  constructor(private albumService: AlbumService) {}

  ngOnInit(): void {
    this.loadAlbums();
  }

  loadAlbums() {
    this.loading = true;
    this.errorMsg = '';

    this.albumService.getAlbums()
      .pipe(
        catchError(() => {
          this.errorMsg = 'Failed to load albums.';
          return of([]);
        }),
        finalize(() => (this.loading = false))
      )
      .subscribe((data: Album[]) => {
        this.albums = data;
      });
  }

  deleteAlbum(id: number) {
    this.albumService.deleteAlbum(id).subscribe(() => {
      this.albums = this.albums.filter(a => a.id !== id);
    });
  }
}
