//
//  LaunchesList.swift
//  HackUTD-SpaceXLaunches
//
//  Created by Nihaal Manesia on 11/11/24.
//

import SwiftUI

struct LaunchesList: View {
    @State private var launches: [Launch] = []
    @State private var searchText: String = ""
    
    var searchResults: [Launch] {
        if searchText.isEmpty {
            return launches
        } else {
            return launches.filter { launch in
                return launch.name.localizedCaseInsensitiveContains(searchText)
            }
        }
    }
    
    var body: some View {
        NavigationStack {
            List {
                if launches.isEmpty {
                    ContentUnavailableView {
                        Label {
                            Text("Fetching launches")
                        } icon: {
                            ProgressView().progressViewStyle(.circular)
                        }
                    }
                    .onAppear(perform: {
                        Task {
                            do {
                                try await fetchLaunches()
                            } catch {
                                debugPrint(error)
                            }
                        }
                    })
                } else if searchResults.isEmpty {
                    ContentUnavailableView {
                        Label {
                            Text("No results found")
                        } icon: {
                            Text("👽")
                                .font(.system(size: 100))
                        }
                    }
                } else {
                    ForEach(searchResults) { launch in
                        NavigationLink {
                            LaunchDetailView(launch: launch)
                        } label: {
                            VStack(alignment: .leading) {
                                Text(launch.name)
                                    .font(.title2)
                                Text(launch.dateUnix.toString())
                                    .lineLimit(1)
                                    .font(.subheadline)
                                    .foregroundStyle(.secondary)
                            }
                        }
                    }
                }
            }
            .navigationTitle("Launches")
            .searchable(text: $searchText)
        }
    }
    
    func fetchLaunches() async throws {
        if let url = URL(string: "https://api.spacexdata.com/v4/launches") {
            let (data, _) = try await URLSession.shared.data(from: url)
            let decoder = JSONDecoder()
            decoder.keyDecodingStrategy = .convertFromSnakeCase
            decoder.dateDecodingStrategy = .secondsSince1970
            let launches = try decoder.decode([Launch].self, from: data)
            await MainActor.run {
                self.launches = launches
            }
        }
    }
}

#Preview {
    LaunchesList()
}
