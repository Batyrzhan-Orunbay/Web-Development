# Album Browser — Lab 6: Routing & HTTP

A multi-page Single Page Application (SPA) built with Angular that lets you browse, view, edit, and delete albums from the JSONPlaceholder REST API.

## Features

- **6 routes**: Home, About, Albums list, Album detail, Album photos + 404 redirect
- **AlbumService**: Centralized HTTP service with `getAlbums`, `getAlbum`, `getAlbumPhotos`, `updateAlbum`, `deleteAlbum`
- **CRUD**: Read (list & detail), Update (edit title), Delete (remove from list)
- **Responsive photo grid** with hover overlay
- **Loading indicators** and error/empty state handling
- **TypeScript interfaces** for `Album` and `Photo` models

## Getting Started

### Prerequisites

- Node.js >= 18.x
- npm >= 9.x
- Angular CLI: `npm install -g @angular/cli`

### Installation

```bash
cd lab6/album-browser
npm install
```

### Run Development Server

```bash
ng serve
```

Navigate to `http://localhost:4200/`. The app reloads automatically on file changes.

### Build for Production

```bash
ng build
```

Output will be in the `dist/` folder.

## Project Structure

```
src/
├── app/
│   ├── models/
│   │   ├── album.model.ts       # Album interface
│   │   └── photo.model.ts       # Photo interface
│   ├── services/
│   │   └── album.service.ts     # HTTP service for API calls
│   ├── components/
│   │   ├── home/                # HomeComponent
│   │   ├── about/               # AboutComponent
│   │   ├── albums/              # AlbumsComponent (list)
│   │   ├── album-detail/        # AlbumDetailComponent
│   │   └── album-photos/        # AlbumPhotosComponent
│   ├── app.component.*          # Root component with navbar
│   ├── app.routes.ts            # Route configuration
│   └── app.config.ts            # App configuration (providers)
├── index.html
├── main.ts
└── styles.css
```

## API

Uses [JSONPlaceholder](https://jsonplaceholder.typicode.com) — a free fake REST API.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/albums` | All albums |
| GET | `/albums/:id` | Single album |
| GET | `/albums/:id/photos` | Album photos |
| PUT | `/albums/:id` | Update album (simulated) |
| DELETE | `/albums/:id` | Delete album (simulated) |

> Note: PUT and DELETE are simulated by JSONPlaceholder — changes are not persisted server-side, but the UI updates locally.

## Course

- **Course**: Web Development
- **Lab**: Lab 6 — Routing & HTTP
- **Student**: Your Name Here
