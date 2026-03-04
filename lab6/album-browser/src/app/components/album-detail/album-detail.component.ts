import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AlbumService } from '../../services/album.service';
import { Album } from '../../models/album.model';

@Component({
  selector: 'app-album-detail',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './album-detail.component.html',
  styleUrl: './album-detail.component.css'
})
export class AlbumDetailComponent implements OnInit {
  album: Album | null = null;
  editTitle = '';
  loading = true;
  saving = false;
  saveSuccess = false;
  error: string | null = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private albumService: AlbumService
  ) {}

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.albumService.getAlbum(id).subscribe({
      next: (data) => {
        this.album = data;
        this.editTitle = data.title;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load album details.';
        this.loading = false;
        console.error(err);
      }
    });
  }

  saveAlbum(): void {
    if (!this.album) return;
    this.saving = true;
    const updated: Album = { ...this.album, title: this.editTitle };
    this.albumService.updateAlbum(updated).subscribe({
      next: () => {
        this.album = updated;
        this.saving = false;
        this.saveSuccess = true;
        setTimeout(() => this.saveSuccess = false, 2500);
      },
      error: (err) => {
        this.saving = false;
        console.error('Failed to update album:', err);
      }
    });
  }

  goToPhotos(): void {
    if (this.album) {
      this.router.navigate(['/albums', this.album.id, 'photos']);
    }
  }

  goBack(): void {
    this.router.navigate(['/albums']);
  }
}
