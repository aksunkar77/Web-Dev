import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { catchError, finalize, of, switchMap, tap } from 'rxjs';

import { AlbumService } from '../services/album.service';
import { Album } from '../models/album.model';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './album-detail.html',
  styleUrl: './album-detail.css'
})
export class AlbumDetail implements OnInit {
  albumId = 0;

  album: Album | null = null;
  title = '';

  loading = false;
  saving = false;
  errorMsg = '';

  constructor(
    private route: ActivatedRoute,
    private albumService: AlbumService
  ) {}

  ngOnInit(): void {
    this.route.paramMap
      .pipe(
        tap(() => {
          this.loading = true;
          this.errorMsg = '';
          this.album = null;
        }),
        switchMap(params => {
          const rawId = params.get('id');
          console.log('Route ID (raw):', rawId);

          this.albumId = Number(rawId);
          console.log('Route ID (number):', this.albumId);

          if (!Number.isFinite(this.albumId) || this.albumId <= 0) {
            this.errorMsg = 'Invalid album id in URL.';
            return of(null as Album | null);
          }

          return this.albumService.getAlbum(this.albumId).pipe(
            catchError((err) => {
              console.error('DETAIL API ERROR:', err);
              this.errorMsg = 'Failed to load album details.';
              return of(null as Album | null);
            })
          );
        }),
        finalize(() => (this.loading = false))
      )
      .subscribe((data: Album | null) => {
        console.log('DETAIL DATA:', data);
        this.album = data;
        if (data) this.title = data.title;
      });
  }

  save(): void {
    if (!this.album) return;

    this.saving = true;
    const updated: Album = { ...this.album, title: this.title };

    this.albumService.updateAlbum(updated)
      .pipe(
        catchError((err) => {
          console.error('UPDATE API ERROR:', err);
          this.errorMsg = 'Failed to save album title.';
          return of(null as Album | null);
        }),
        finalize(() => (this.saving = false))
      )
      .subscribe((res: Album | null) => {
        if (res) this.album = updated;
      });
  }
}